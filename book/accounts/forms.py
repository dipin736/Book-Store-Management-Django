from django import forms
from .models import Book,Order

class BookModelForm(forms.ModelForm):
    """Form definition for BookModel."""

    class Meta:
        """Meta definition for BookModelform."""

        model = Book
        fields = '__all__'

class OrderModelForm(forms.ModelForm):
    """Form definition for OrderModel."""

    class Meta:
        """Meta definition for OrderModelform."""

        model = Order
        fields = ['name', 'email', 'mobile', 'address', 'city', 'pincode']

        

class OrderForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Order
        fields=['status']
