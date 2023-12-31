from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import User,Request_Book
from .forms import UserForm
from accounts.models import Book, Cart,Category, Wishlist
from django.contrib.auth.decorators import login_required
from .filters import ProductFilter


# Create your views here.


def account_login(request):
    # if request.method == 'GET':
    #     return render(request,'user_login.html')
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in") 
        return redirect('display')
    else:
        if request.method == 'POST':
            uname = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=uname,password=password)
            if user is not None:
                login(request,user)
                if user.is_superuser==True:
                    # messages.success(request, "Logged in as admin.")
                    return redirect('admin_base')
                else:
                    messages.success(request, "Welcome, you have successfully logged in.") 
                    return redirect('display')
            else:
                messages.error(request, "Please Enter a valid username and password")
                return redirect('account_login')

        return render(request, "user_login.html")
    

# def account_logout(request):
#     logout(request)
#     return redirect('account_login')

def account_register(request):
    if request.method == 'GET':
        context = {
            'form':UserForm()
        }
        return render(request,'user_register.html',context)
    elif request.method == 'POST':
        user = UserForm(request.POST,request.FILES)
        if user.is_valid():
            obj = user.save(commit=False)
            obj.user_type = 'user'
            obj.set_password(user.cleaned_data['password'])
            obj.save()
            return redirect('account_login')
        else:
            context={
                'form':user
            }
            return render(request,'user_register.html',context)

# def user_home(request):
#     return render(request,'user_home.html')


def logoutuser(request):
    logout(request)
    messages.success(request, "Logout successfully .") 
    return redirect('account_login')

@login_required(login_url='user_login')
def userprofile(request):
    return render(request,'user_profile.html')


# def viewuser(request):
#     data=User.objects.all()
#     context = {
#         'data': data
#     }
#     return render(request,'user_profile.html',context)

@login_required(login_url='account_login')
def account_update(request):
    user = User.objects.get(id=request.user.id)

    # Calculate counts
    cart_item_count = Cart.objects.filter(user=request.user).count()
    wish_item_count = Wishlist.objects.filter(user=request.user).count()

    if request.method == 'GET':
        context = {
            'form': UserForm(instance=user),
            'cart_item_count': cart_item_count,
            'wish_item_count': wish_item_count,
        }
        return render(request, 'update.html', context)
    elif request.method == 'POST':
        userform = UserForm(request.POST, request.FILES, instance=user)
        if userform.is_valid():
            obj = userform.save(commit=False)
            obj.user_type = 'user'
            obj.set_password(userform.cleaned_data['password'])
            obj.save()
            return redirect('display')
        else:
            context = {
                'form': userform,
                'cart_item_count': cart_item_count,
                'wish_item_count': wish_item_count,
            }
            return render(request, 'update.html', context)
        

def request_books(request):
    if request.method == "POST":
        user = request.user
        book_name = request.POST.get('book_name')
        author = request.POST.get('author')
        if not book_name or not author:
            messages.error(request, 'Both book name and author are required.')
        else:
            # Save book if validation passes
            book = Request_Book(user=user, book_name=book_name, author=author)
            book.save()
            messages.success(request, 'Book request submitted successfully.')
    # Calculate counts
    cart_item_count = Cart.objects.filter(user=request.user).count()
    wish_item_count = Wishlist.objects.filter(user=request.user).count()

    context = {
        'cart_item_count': cart_item_count,
        'wish_item_count': wish_item_count,
    }

    return render(request, "request_books.html", context)

def requested_books(request):
    requested_book = Request_Book.objects.all()
    return render(request, "requested_books.html", {'requested_book':requested_book})

def delete_books(request, id):
    delete_book = Request_Book.objects.get(id=id)
    delete_book.delete()
    return redirect('requested_books')


