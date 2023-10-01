from django.db import models
from django.contrib.auth.models import User

#Vendor Models
class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField()
    address = models.TextField(max_length=400) 
    email = models.EmailField()
    def __str__(self):
        return self.user.username

#Product Category Model
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.title

#Product
class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null = True, related_name='category_products')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    price = models.FloatField()
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null = True)
    def __str__(self):
        return self.title
    
#Customer Model
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField()
    address = models.TextField(max_length=400) 
    email = models.EmailField()
    def __str__(self):
        return self.user.username

#Order Model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_orders')
    order_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % (self.order_time)


#OrderItems Model
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title


#Customer Address Model
class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_address')
    address = models.TextField()
    default_address = models.BooleanField(default=False)

    def __str__(self):
        return self.address
    
#Product Rating & Reviews
class ProductRating(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='rating_customers')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name= 'product_ratings')
    rating = models.IntegerField()
    reviews = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating} - {self.reviews}'