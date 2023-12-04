from django.db import models
from user.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering=['name']

class Book(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    image=models.FileField(max_length=100,upload_to='Upload', null=True, blank=True)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2 ,validators=[MinValueValidator(1)])  # Use DecimalField for price
    stock = models.IntegerField(default=0,validators=[MinValueValidator(1)])
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['title']
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE, null=True, blank=True)
    quantity=models.IntegerField(default=0)
    added_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'
    
    @property
    def total_cost(self):
        return self.quantity * self.book.price
    
    @staticmethod
    def total_cost_of_products(cart_items):
        total_cost = 0
        for item in cart_items:
            total_cost += item.total_cost
        return total_cost

class Order(models.Model):
   
    PAYMENT=(
        ('Credict Card','Credict Card'),
        ('G-Pay','G-pay'),
        ('Paypal','Paypal'),

    ) 
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50,null=False)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50,null=False)
    pincode = models.CharField(max_length=50,null=False)
    total_price = models.FloatField(null=True,default=0.0)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    payment_id=models.CharField(max_length=50,null=True)
    tracking_no=models.CharField(max_length=50,null=True)
    status=models.BooleanField(max_length=50,default=False)
    payment_method = models.CharField(max_length = 20,choices=PAYMENT ,default='Paypal')

    def __str__(self):
        return f'{self.id, self.tracking_no}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'Order Item ID: {self.id}, Order ID: {self.order.tracking_no}'




class  review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_desp = models.CharField(max_length=100)
    rating = models.IntegerField()
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.review_desp}'


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
