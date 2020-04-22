from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    address = models.TextField()
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=255, unique=True)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    item_type = models.CharField(max_length=255)
    purchase_price = models.DecimalField(max_digits=8, decimal_places=2)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2)
    supplier_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)

class Stock(models.Model):
    color = models.CharField(max_length=255)
    amount = models.IntegerField()
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)

class Order(models.Model):
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    create_date = models.DateTimeField(auto_now=True)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cus_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Order_Item(models.Model):
    amount = models.IntegerField()
    color = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)