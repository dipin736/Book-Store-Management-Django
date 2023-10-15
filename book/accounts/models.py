from django.db import models
from user.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    image=models.FileField(max_length=100,upload_to='Upload', null=True, blank=True)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    stock = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE, null=True, blank=True)
    quantity=models.CharField(max_length=10,default=1)
    added_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
    


class Order(models.Model):
   

    PAYMENT=(
        ('Credict Card','Credict Card'),
        ('G-Pay','G-pay'),
        ('Paypal','Paypal'),

    )
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500)
    mobile = models.CharField(max_length=20)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(max_length=50,default=False)
    payment_method = models.CharField(max_length = 20,choices=PAYMENT)


    def __str__(self):
        return self.user.username

class  review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_desp = models.CharField(max_length=100)
    rating = models.IntegerField()
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username