from django import forms
from .models import User

class UserForm(forms.ModelForm):
    """Form definition for User."""
    password = forms.CharField(
        widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput()
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('first_name','last_name','email','phone','username','photo','address')

    def clean(self):
        clean_data = super(UserForm,self).clean()
        password = clean_data.get('password')
        confirm_password = clean_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Password and confirm password doesnt match!')