from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('contact/',contact,name="contact"),
    path('about/',about,name='about'),
    path('admin_base/',admin_base,name='admin_base'),
    path('logout/',admin_logout,name='admin_logout'),

    # ...........................CATEGORY....................

    path('add_category/',add_category,name='add_category'),
    path('view_category',view_category,name='view_category'),
    path('edit_category/<int:id>/',edit_category,name='edit_category'),
    path('delete_category/<int:id>/',delete_category,name='delete_category'),

    # ...........................PRODUCT....................
    path('view_product/',view_product,name='view_product'),
    path('add_product/',add_product,name='add_product'),
    path('edit_product/<int:id>',edit_product,name='edit_product'),
    path('delete_product/<int:id>/', delete_product, name="delete_product"),

    # ...........................USER....................
    path('view_user/',view_user,name='view_user'),
    path('delete_user/<int:id>/',delete_user,name='delete_user'),

    # ...........................HOME....................
    path('display/',display,name='display'),
    path('sidebar/<int:id>/',sidebar,name='sidebar'),
    path('get_cart_data/',get_cart_data,name='get_cart_data'),

    # ...........................ADMIN SIDE....................

    path('admin_view_booking/',admin_view_booking,name='admin_view_booking'),
    path('admin_view_booking/<str:t_no>/',admin_view_orders,name='admin_view_orders'),


    # ...........................CART,ORDER-VIEW....................
    path('update_order/<int:id>',update_order_view,name='update_order_view'),
    path('delete_order/<int:id>',delete_order,name='delete_order'),
    path('book/<int:id>/',book_details, name='book_details'),

    # CART
    path('add-to-cart',addtocart,name='addtocart'),
    path('viewcart/',viewcart,name='cart'),
    path('delete-from-cart/<int:cart_item_id>/',delete_cart_item, name='delete_cart_item'),     
    path('update-cart',updatecart,name='updatecart'),
    
    # ORDER

    path('booking/',booking,name='booking'),
    path('view-order/',view_order,name='view_order'),
    path('view-my-order/<str:t_no>/',view_my_order, name='view_my_order'),

    # WISHLIST

    path('wishlist/',wishlist,name='wishlist'),
    path('add-to-wishlist',addtowishlist,name='addtowishlist'),
    path('delete-from-wishlist/<int:wish_item_id>/',delete_wish_item, name='delete_wish_item'),     

    path('pdfajax',pdfajax,name='pdfajax'),
    path('search/', search_books, name='search_books'),





    

]