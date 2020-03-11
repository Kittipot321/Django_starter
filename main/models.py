from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.PROTECT,null=True)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    def __str__(self):
        return self.name
 
class Order(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    total_price = models.FloatField()
    products = models.ManyToManyField(Product,through='Order_Products')

class Order_Products(models.Model):
    amount = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class My_Cart(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)