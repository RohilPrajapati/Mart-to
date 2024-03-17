from rest_framework import serializers
from .models import Product

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class ProductCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    stock = serializers.IntegerField()
    description = serializers.CharField()
    image = serializers.ImageField()
    price = serializers.DecimalField(max_digits=9,decimal_places=2)
    status = serializers.BooleanField()


