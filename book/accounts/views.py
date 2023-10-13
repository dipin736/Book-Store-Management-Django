from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category,Book,Cart,Order
from .forms import BookModelForm,OrderModelForm,OrderForm
from user.models import User
from django.http import JsonResponse
from django.core.mail import send_mail

# Create your views here.



def home(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'shared/about.html')

def contact(request):
    if request.method=='POST':
        message_name=request.POST['name']
        message_email=request.POST['email']
        message=request.POST['message']
        send_mail(
            message_name,
            message,
            message_email,
            ['dipinkarunakaran6@gmail.com'],
        )
        return render(request, 'shared/contact.html')
    else:
       return render(request, 'shared/contact.html')





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


@login_required
def view_user(request,):
    customers=User.objects.all()
    return render(request,'view_user.html',{'customers':customers})


@login_required(login_url='account_login')
def display(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    context = {
        'categories': categories,
        'books': books,
    }
    return render(request, 'display.html', context)


@login_required(login_url='account_login')
def delete_user(request, id):
    customers=User.objects.get(id=id)
    customers.delete()
    return redirect('view_user')

@login_required(login_url='account_login')

@login_required(login_url='account_login')
def sidebar(request, id):
    selected_category = get_object_or_404(Category, id=id)
    categories = Category.objects.all()
    books = Book.objects.filter(category=selected_category)  # Filter books based on the selected category

    context = {
        'selected_category': selected_category,
        'categories': categories,
        'books': books,
    }

    return render(request, 'display.html', context)


@login_required(login_url='account_login')
def add_to_cart(request,id):
    user=User.objects.get(id=request.user.id)
    book=Book.objects.get(id=id)
    cart=Cart(user_id=user.id,book_id=book.id)
    cart.save()
    context={
        'cart':cart
    }
    return render(request,'cart.html',context)

# def viewcart(request):
#     cart=Cart.objects.all()
#     context={
#         'cart':cart
#     }
#     return render(request,'viewcart.html',context)

@login_required(login_url='account_login')
def delete_cart(request,id):
    cart=Cart.objects.filter(id=id)
    cart.delete()
    return redirect("viewcart")

@login_required(login_url='user_login')
def get_cart_data(request):
    cart=Cart.objects.filter(user_id=request.user.id)
    price,items=0,0
    for i in cart :
        price=int(i.book.price)
        items=int(i.quantity)
    res={
        'price':price,'items':items,
    }
    return JsonResponse(res)

import razorpay

@login_required(login_url='account_login')

def booking(request,id): 
    # form=OrderModelForm()
    user=User.objects.get(id=request.user.id)
    book=Book.objects.get(id=id)
    form=OrderModelForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            order=form.save(commit=False)
            order.user=User.objects.get(id=request.user.id)
            order.book=Book.objects.get(id=book.id)   
            print(order) 
            order.status=False
            order.save()      
            return redirect('display')	
    
        client = razorpay.Client(auth=("rzp_test_tIYSGqIfPmDOgX", "8SLCoYyRitptnvJsazcwC4gG"))
        DATA = {
        "amount":'0',
        "currency": "INR",
        "receipt": "receipt#1",
        "notes": {
            "key1": "value3",
            "key2": "value2"
                }
            }
        client.order.create(data=DATA)
    return render(request, 'booking.html', {"form": form})


@login_required(login_url='account_login')
def view_order(request):
    myorder = Order.objects.filter(user_id= request.user.id)
    return render(request, 'view_order.html', {"myorder": myorder})


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

def admin_view_booking(request):
    myorder = Order.objects.all()
    return render(request, 'admin-view-booking.html', {"myorder": myorder})

def delete_order(request,id):
    myorder=Order.objects.filter(id=id)
    myorder.delete()
    return redirect("admin_view_booking")

