from django import forms
from .models import Book,Order

class BookModelForm(forms.ModelForm):
    """Form definition for BookModel."""

    class Meta:
        """Meta definition for BookModelform."""

        model = Book
        fields = '__all__'

# forms.py
class OrderModelForm(forms.ModelForm):
    """Form definition for OrderModel."""

    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'id': 'id_name'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'id': 'id_email'}))
    mobile = forms.CharField(label="Mobile", widget=forms.TextInput(attrs={'id': 'id_mobile'}))
    address = forms.CharField(label="Address", widget=forms.TextInput(attrs={'id': 'id_address'}))
    city = forms.CharField(label="City", widget=forms.TextInput(attrs={'id': 'id_city'}))
    pincode = forms.CharField(label="Pincode", widget=forms.TextInput(attrs={'id': 'id_pincode'}))

    class Meta:
        """Meta definition for OrderModel form."""

        model = Order
        fields = ['name', 'email', 'mobile', 'address', 'city', 'pincode']


class OrderForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Order
        fields=['status']
