from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('contact/',contact,name="contact"),
    path('about/',about,name='about'),
    path('admin_base/',admin_base,name='admin_base'),
    path('logout/',admin_logout,name='admin_logout'),


    path('add_category/',add_category,name='add_category'),
    path('view_category',view_category,name='view_category'),
    path('edit_category/<int:id>/',edit_category,name='edit_category'),
    path('delete_category/<int:id>/',delete_category,name='delete_category'),

    path('view_product/',view_product,name='view_product'),
    path('add_product/',add_product,name='add_product'),
    path('edit_product/<int:id>',edit_product,name='edit_product'),
    path('delete_product/<int:id>/', delete_product, name="delete_product"),

    path('view_user/',view_user,name='view_user'),
    path('delete_user/<int:id>/',delete_user,name='delete_user'),

    path('display/',display,name='display'),
    path('sidebar/<int:id>/',sidebar,name='sidebar'),
    # path('checkout/<int:id>/',buynow,name='buynow'),
    
    path('add_to_cart/<int:id>/',add_to_cart,name='add_to_cart'),
    # path('viewcart/',viewcart,name='viewcart'),
    path('delete_cart/<int:id>/',delete_cart,name='delete_cart'),
    path('get_cart_data/',get_cart_data,name='get_cart_data'),


    path('booking/<int:id>/',booking,name='booking'),
    path('view_order/',view_order,name='view_order'),
    path('admin_view_booking/',admin_view_booking,name='admin_view_booking'),
    path('update_order/<int:id>',update_order_view,name='update_order_view'),
    path('delete_order/<int:id>',delete_order,name='delete_order'),


    path('book/<int:id>/',book_details, name='book_details'),

    







    

]