import django_filters
from accounts.models import Book

# class ProductFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr='icontains')
#     price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
#     price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

#     class Meta:
#         model = Book
#         fields = ['title']

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title']
