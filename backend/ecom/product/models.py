from django.db import models
from users.models import User

class Product(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField()
    image = models.ImageField(upload_to= 'product')
    price = models.DecimalField(max_digits=9,decimal_places=2)
    status = models.BooleanField(default=True)
    stock = models.IntegerField()
    entry_date = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,related_name="created_by",null=True)
    update_date = models.DateTimeField(null=True)
    update_by = models.ForeignKey(User, on_delete=models.PROTECT,related_name="update_by",null=True)


