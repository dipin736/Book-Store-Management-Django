from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.BigIntegerField(
        verbose_name='Contact Number',
        default=0
    )

    user_type = models.CharField(
        max_length=20,
        default='admin'
    )
    
    photo = models.FileField(
        verbose_name='Upload Profile Photo',
        max_length=2000,
        upload_to='Upload',
        default='No Image'
    )

    address=models.TextField(
        verbose_name='Address',
        max_length=100,
        default='address'
    )


class Request_Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    
    def __str__ (self):
        return self.book_name
    
