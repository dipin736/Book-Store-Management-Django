from django.conf import settings
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Category,Book,Cart,Order, review,OrderItem,Wishlist
from .forms import BookModelForm,OrderModelForm,OrderForm
from user.models import User
from django.http import JsonResponse
from django.core.mail import send_mail
from django.db.models import Avg, Count
import uuid
from django.contrib import messages


# Create your views here.

# .....HOME/HEADER/FOOTER .............. starts
def home(request):
    return render(request, 'base.html')
def about(request):
    return render(request, 'shared/about.html')


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        user_message = request.POST['message']

        # Customize the email message format
        email_subject = f'Message from {message_name}'
        email_message = f'''
        You have received a new message from the contact form:

        Name: {message_name}
        Email: {message_email}

        Message:
        {user_message}
        '''

        send_mail(
            email_subject,
            email_message,
            settings.EMAIL_HOST_USER,  # Sender's email
            [message_email],  # Recipient's email
            fail_silently=False
        )
        return render(request, 'shared/contact.html')
    else:
        return render(request, 'shared/contact.html')


    
# .....HOME/HEADER/FOOTER.............. end



# ...... ADMIN SIDE FUNCTIONS.....starts
def admin_logout(request):
    logout(request)
    return redirect('home')

@login_required
def admin_base(request):
    book=Book.objects.all()
    order=Order.objects.all()
    user=User.objects.all()
    total_books=book.count()
    total_order=order.count()
    total_user=user.count()

    context={
        'book':book,
        'total_books':total_books,
        'total_order':total_order,
        'total_user':total_user,
    }
    return render(request,'admin_base.html',context)


# ................ ADMIN SIDE FUNCTIONS................starts


# ......................CATEGORY...................... starts
@login_required
def add_category(request):
    if request.method == "POST":
        name = request.POST['name']
        Category.objects.create(name=name)
        msg='category added'
    return render(request, 'store/add_category.html')

def view_category(request):
    context={
        'category':Category.objects.all(),
        }
    return render(request,'store/view_category.html',context)

@login_required
def edit_category(request,id):
    category=Category.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        category.name = name
        print(name)
        category.save()
    return render(request, 'store/edit_category.html')

def delete_category(request,id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('view_category')

# ....................CATEGORY..................... ends


# .......................BOOKS...............starts
@login_required
def add_product(request):
    # form=BookModelForm()
    form=BookModelForm(request.POST,request.FILES)
    if request.method=='POST':
        # form=BookModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_product')
    context={'form':form  }
    return render(request,'store/add_product.html',context)

def view_product(request):
    book=Book.objects.all()
    context={ 'book':book  }
    return render(request,'store/view_product.html',context)

@login_required
def edit_product(request,id):
    book=Book.objects.get(id=id)
    form=BookModelForm(instance=book)
    if request.method=='POST':
        form=BookModelForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('view_product')
    context={'form':form }
    return render(request,'store/edit_product.html',context)

@login_required
def delete_product(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('store/view_product')
# .........................BOOKS..........................end


# .................USER HOME..........starts

@login_required
def view_user(request,):
    customers=User.objects.all()
    return render(request,'view_user.html',{'customers':customers})


# ............HOME PAGE BOOKS..........

@login_required(login_url='account_login')
def display(request):
    categories = Category.objects.all()
    books = Book.objects.annotate(avg_rating=Avg('review__rating'), num_reviews=Count('review'))
    cart_item_count = Cart.objects.filter(user=request.user).count()
    wish_item_count = Wishlist.objects.filter(user=request.user).count()
    context = {
        'categories': categories,
        'books': books,
        'cart_item_count': cart_item_count,
        'wish_item_count': wish_item_count,

    }
    return render(request, 'display.html', context)

# ................VIEW SINGLE BOOK..........
def book_details(request, id):
    book = get_object_or_404(Book, id=id)
    categories = book.category.name
    reviews = review.objects.filter(book=book)
    related_books = Book.objects.filter(category=book.category).exclude(id=id)[:3]  # Exclude the current book from related books
    cart_item_count = Cart.objects.filter(user=request.user).count()
    wish_item_count = Wishlist.objects.filter(user=request.user).count()
      


    if request.method == 'POST':
        user = request.user
        star_rating = request.POST['rate']
        review_text = request.POST['review_desp']

        if star_rating and review_text:
            review_instance = review(user=user, book=book, rating=star_rating, review_desp=review_text)
            review_instance.save()

            return redirect('book_details', id=book.id)
            # Redirect to the same product details page after the review is submitted
    
    context = {
        'book': book,
        'categories':categories,
        'related_books': related_books,
        'reviews': reviews,
        'cart_item_count': cart_item_count,
        'wish_item_count': wish_item_count,

    }
    return render(request, 'book_details.html', context)

@login_required(login_url='account_login')
def delete_user(request, id):
    customers=User.objects.get(id=id)
    customers.delete()
    return redirect('view_user')

@login_required(login_url='account_login')
def sidebar(request, id):
    selected_category = get_object_or_404(Category, id=id)
    categories = Category.objects.all()
    books = Book.objects.filter(category=selected_category)  # Filter books based on the selected category
    cart_item_count = Cart.objects.filter(user=request.user).count()
    wish_item_count = Wishlist.objects.filter(user=request.user).count()

    context = {
        'selected_category': selected_category,
        'categories': categories,
        'books': books,
        'cart_item_count': cart_item_count,
        'wish_item_count': wish_item_count,


    }

    return render(request, 'display.html', context)


# @login_required(login_url='account_login')
# def add_to_cart(request,id):
#     user=User.objects.get(id=request.user.id)
#     book=Book.objects.get(id=id)
#     cart=Cart(user_id=user.id,book_id=book.id)
#     cart.save()
#     context={
#         'cart':cart
#     }
#     return render(request,'cart.html',context)


# ......................ADD TO CART..................... 
def addtocart(request):
    if request.method == 'POST':
        print(request.POST) 
        book_id = request.POST.get('book_id')
        book_qty = request.POST.get('book_qty')
        
        # Check if book_id and book_qty are present
        if book_id is None or book_qty is None:
            return JsonResponse({'status': 'Invalid request parameters'})
        # Try to convert book_id and book_qty to integers
        try:
            book_id = int(book_id)
            book_qty = int(book_qty)
        except (ValueError, TypeError):
            return JsonResponse({'status': 'Invalid request parameters'})

        # Query the database for the book with the given book_id
        book = get_object_or_404(Book, id=book_id)
       

        # Check if the requested quantity is available in stock
        if book.stock >= book_qty:
            # Check if the product is already in the cart
            if Cart.objects.filter(user=request.user, book=book).exists():
                return JsonResponse({'status': 'Product Already in Cart'})
            else:
                # Create a new cart item
                Cart.objects.create(user=request.user, book=book, quantity=book_qty)
                cart_item_count = Cart.objects.filter(user=request.user).count()
                request.session['cart_item_count'] = cart_item_count
                response_data = {
                        'status': 'Product added successfully',
                        'cart_item_count': cart_item_count,
                }
                return JsonResponse(response_data)
        else:
            return JsonResponse({'status': f'Only {book.stock} quantity available'})

    # Invalid request method
    return redirect(book_details)

# .........................VIEW CART......................
def viewcart(request):
    cart=Cart.objects.filter(user=request.user)
    cart_item_count = Cart.objects.filter(user=request.user).count()
    wish_item_count = Wishlist.objects.filter(user=request.user).count()

    total_cost = Cart.total_cost_of_products(cart)
    context={
        'cart':cart,
         'cart_item_count': cart_item_count,
         'total_cost': total_cost,
            'wish_item_count': wish_item_count,

    }
    return render(request,'viewcart.html',context)


# ...........................UPDATE CART....................
def updatecart(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        book_id = int(request.POST.get('book_id'))
        book_qty = int(request.POST.get('book_qty'))

        # Get the Cart object for the given book and user
        cart_item = get_object_or_404(Cart, user=request.user, book_id=book_id)

        # Update the quantity and save the Cart object
        cart_item.quantity = book_qty
        cart_item.save()

        return JsonResponse({'status': 'Updated successfully'})
    else:
        return JsonResponse({'status': 'Invalid request'})


# ...........................DELETE CART....................
def delete_cart_item(request, cart_item_id):
    try:
        print(f'Deleting cart item {cart_item_id}')
        cart_item = Cart.objects.get(id=cart_item_id, user=request.user)
        cart_item.delete()
        return JsonResponse({'status': 'success'})
    except Cart.DoesNotExist:
        print('Cart item not found')
        return JsonResponse({'status': 'error', 'message': 'Cart item not found'}, status=400)
    except Exception as e:
        print(e)  # Log the exception for debugging purposes
        return JsonResponse({'status': 'error', 'message': 'Error deleting cart item'}, status=500)




@login_required(login_url='user_login')
def get_cart_data(request):
    cart=Cart.objects.filter(user=request.user.id)
    price,items=0,0
    for i in cart :
        price=int(i.book.price)
        items=int(i.quantity)
    res={
        'price':price,'items':items,
    }
    return JsonResponse(res)




# ...........................ORDER PAGE....................
from django.views.decorators.csrf import csrf_protect
@login_required(login_url='account_login')
@csrf_protect
def booking(request):
    form = OrderModelForm()
    order_placed = False
    order = None

    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.status = False
            order.tracking_no = str(uuid.uuid4().fields[-1])[:6].upper()

            cart_items = Cart.objects.filter(user=request.user)
            total_cost = Cart.total_cost_of_products(cart_items)
            order.total_price = total_cost
            order.save()
            order_placed = True
            messages.success(request, f"Order placed successfully! Your tracking number is {order.tracking_no}.")

            if order.payment_method == 'Pay by Razor Pay':
                return JsonResponse({'status': "Your order has been successfully"})

            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    book=cart_item.book,
                    price=cart_item.book.price,
                    quantity=cart_item.quantity
                )

            cart_items.delete()

            return redirect('display')
        else:
            print('error', form.errors)

    cart_items = Cart.objects.filter(user=request.user)
    total_cost = Cart.total_cost_of_products(cart_items)
    cart_item_count = Cart.objects.filter(user=request.user).count()
    wish_item_count = Wishlist.objects.filter(user=request.user).count()

    return render(request, 'booking.html', {
        'form': form,
        'cart_items': cart_items,
        'total_cost': total_cost,
        'order_placed': order_placed,
        'order': order,
        'cart_item_count': cart_item_count,
        'wish_item_count': wish_item_count
    })

# razor pay
import razorpay


def razorpaycheck(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_cost=0
    for item in cart_items:
        total_cost = total_cost + item.book.price*item.quantity

    razorpay_key = settings.RAZORPAY_ID

    return JsonResponse({
        "total_cost":total_cost,
        "razorpay_key": razorpay_key
    })




# ...........................VIEW ORDER....................
@login_required(login_url='account_login')
def view_order(request):
    orders=Order.objects.filter(user=request.user)
    cart_item_count = Cart.objects.filter(user=request.user).count()
    wish_item_count = Wishlist.objects.filter(user=request.user).count()


    return render(request, 'view_order.html', {"orders": orders,'cart_item_count':cart_item_count,'wish_item_count': wish_item_count,
})


# ...........................VIEW ORDERED ITEM....................
def view_my_order(request, t_no):
    order = get_object_or_404(Order, tracking_no=t_no, user=request.user)
    order_items = OrderItem.objects.filter(order=order)
    cart_item_count = Cart.objects.filter(user=request.user).count()

    context = {"order": order, "order_items": order_items,'cart_item_count':cart_item_count}
    return render(request, 'view_order_details.html', context)


# def view_my_order(request, t_no):
#     order = get_object_or_404(Order, tracking_no=t_no, user=request.user)
#     order_items = OrderItem.objects.filter(order=order)
#     return render(request, 'view_order_details.html', {"order": order, "order_items": order_items})


# ...........................ADMIN UPDATE ORDER ....................
@login_required
def update_order_view(request,id):
    order=Order.objects.get(id=id)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('admin_view_booking')
    return render(request,'store/update_order.html',{'form':form})

# ...........................ADMIN VIEW ORDER ....................
def admin_view_booking(request):
    myorder = Order.objects.all()
    # myorderitem=OrderItem.objects
    return render(request, 'admin-view-booking.html', {"myorder": myorder})

# ...........................ADMIN VIEW ORDERITEM ....................
def admin_view_orders(request,t_no):
    order = get_object_or_404(Order, tracking_no=t_no)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'admin_view_order.html', {"order": order, "order_items": order_items})


# ...........................ADMIN DELETE ORDER ....................
def delete_order(request,id):
    myorder=Order.objects.filter(id=id)
    myorder.delete()
    return redirect("admin_view_booking")


# .............WISHLIST........

def wishlist(request):
    wishlist=Wishlist.objects.filter(user=request.user)
    wish_item_count = Wishlist.objects.filter(user=request.user).count()
    cart_item_count = Wishlist.objects.filter(user=request.user).count()


    context={
        'wishlist':wishlist,
        'wish_item_count': wish_item_count,
        'cart_item_count':  cart_item_count,
    }
    return render(request, 'wishlist.html',context)



from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Book, Wishlist

def addtowishlist(request):
    if request.method == 'POST':
        # Retrieve book_id from the form data
        book_id = request.POST.get('book_id')

        # Check if book_id is present
        if book_id is None:
            return JsonResponse({'status': 'Invalid request parameters'})

        # Try to convert book_id to an integer
        try:
            book_id = int(book_id)
        except (ValueError, TypeError):
            return JsonResponse({'status': 'Invalid request parameters'})

        # Query the database for the book with the given book_id
        book = get_object_or_404(Book, id=book_id)

        # Check if the product is already in the wishlist
        if Wishlist.objects.filter(user=request.user, book=book).exists():
            return JsonResponse({'status': 'Product Already in Wishlist'})
        else:
            # Create a new wishlist item
            Wishlist.objects.create(user=request.user, book=book)
            wish_item_count = Wishlist.objects.filter(user=request.user).count()
            response_data = {
                'status': 'Product added successfully',
                'wish_item_count': wish_item_count,
            }
            return JsonResponse(response_data)

    # Invalid request method
    return JsonResponse({'status': 'Invalid request method'})


def delete_wish_item(request, wish_item_id):
    try:
        wish_item = Wishlist.objects.get(id=wish_item_id, user=request.user)
        wish_item.delete()
        return JsonResponse({'status': 'success'})
    except Wishlist.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Wishlist item not found'}, status=400)
    except Exception as e:
        print(e)  # Log the exception for debugging purposes
        return JsonResponse({'status': 'error', 'message': 'Error deleting Wishlist item'}, status=500)


def pdfajax(request):
    # Filter books based on stock availability
    available_books = Book.objects.filter(stock__gt=0).values_list('title', flat=True)
    book_titles = list(available_books)
    return JsonResponse(book_titles, safe=False)


def search_books(request):
    if request.method == 'POST':
        searcheditem=request.POST.get('title')
        if searcheditem =='':
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            book = Book.objects.filter(title=searcheditem).first()

            if book:
                return redirect('book_details',id=book.id)
            else:
                messages.info(request,'No Product Matched Your Search')
                return redirect(request.META.get("HTTP_REFERER"))
    return redirect(request.META.get("HTTP_REFERER"))

