from django.db import models
from users.models import User
from phonenumber_field.modelfields import PhoneNumberField
from product.models import Product

class Payment(models.Model):
    PAYMENT_CHOICE = [
        ('cash','cash'),
        ('online','online')
    ]
    order_by = models.ForeignKey(User,on_delete=models.PROTECT)
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = PhoneNumberField()
    payment_uid = models.CharField(max_length=100,unique=True)
    total_amt = models.DecimalField(max_digits=9,decimal_places=2)
    transaction_id = models.CharField(max_length=50,null=True)
    payment_method = models.CharField(max_length=10,choices=PAYMENT_CHOICE)
    cancel_status = models.BooleanField(default=False)
    payment_status = models.BooleanField(default=False)
    delivery_status = models.BooleanField(default=False)

class OrderItem(models.Model):
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=9,decimal_places=2)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    payment = models.ForeignKey(Payment,on_delete=models.PROTECT)

