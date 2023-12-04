from django.contrib import admin
from .models import Category,Book,Cart,Order,review
from . import models
from django.db.models import Count

from  django.utils.html import format_html,urlencode
from django.urls import reverse

# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','book_count']
    search_fields=['title']

    def book_count(self,category):
        url= (reverse('admin:accounts_book_changelist') 
              + '?'
              + urlencode({
                  'category__id':str(category.id)
              })) 
        return  format_html('<a href="{}">{}</a>',url,category.book_count)
       
  

    def get_queryset(self, request):
        queryset = super(CategoryAdmin, self).get_queryset(request).annotate(
            book_count=Count('book')
        )
        return queryset
# admin.site.register(Category)

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    autocomplete_fields=['category']
    list_display=['title','category','price']
    list_editable=['price']
    list_filter=['title','updated']
    list_per_page=5
    search_fields=['title__istartswith']

# admin.site.register(Book)

admin.site.register(Cart)

admin.site.register(Order)

admin.site.register(review)






