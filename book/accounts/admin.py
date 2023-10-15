from django.contrib import admin
from .models import Category,Book,Cart,Order,review

# Register your models here.

admin.site.register(Category)

admin.site.register(Book)

admin.site.register(Cart)

admin.site.register(Order)

admin.site.register(review)






