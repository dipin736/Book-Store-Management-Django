from django.urls import path
from .views import *

urlpatterns = [
    path('register/',account_register,name='account_register'),
    path('login/',account_login,name='account_login'),
    # path('user_home/',user_home,name='user_home'),
    path('logout/', logoutuser, name="logoutuser"),
    path('userprofile/',userprofile,name='userprofile'),
    # path('viewuser/',viewuser,name='viewuser'),


    path('userupdate/',account_update,name='account_update'),
    path('request_books/', request_books, name="request_books"),   
    path('requested_books/',requested_books, name='requested_books'),
    path("delete_books/<int:id>/",delete_books, name="delete_books"),

    # path('books/', book_list, name='book_list'),
   path('search/', search_books, name='search_books'),
   


    



]