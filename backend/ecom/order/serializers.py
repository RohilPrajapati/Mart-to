from .models import Payment,OrderItem
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class OrderItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ['payment']
        # fields= '__all__'
        depth=1 


class CombineOrderModelSerializer(serializers.ModelSerializer):
    order_item = serializers.SerializerMethodField()
    class Meta:
        model = Payment
        fields = '__all__'
    def get_order_item(self,obj):
        order_items = OrderItem.objects .filter(payment = obj)
        return OrderItemModelSerializer(order_items,many=True).data




class OrderItemCreateSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=9,decimal_places=2)
    product = serializers.IntegerField()
    # payment = serializers.IntegerField()

class CombineOrderCreateSerializer(serializers.Serializer):
    
    PAYMENT_CHOICE = [
        ('cash','cash'),
        ('online','online')
    ]
    # order_by = serializers.IntegerField()
    username = serializers.CharField()
    address = serializers.CharField()
    contact = PhoneNumberField()
    # payment_uid = serializers.CharField(required=False)
    # total_amt = serializers.IntegerField(required=False)
    # transaction_id = serializers.CharField(required=False)
    payment_method = serializers.ChoiceField(choices=PAYMENT_CHOICE)
    # cancel_status = serializers.BooleanField(default=False)
    # payment_status =serializers.BooleanField(default=False)
    # delivery_status = serializers.BooleanField(default=False)
    order_item = serializers.ListField(child= OrderItemCreateSerializer(),allow_empty=False)

class PaymentPostSerializer(serializers.Serializer):
    oid = serializers.CharField()
    amt = serializers.DecimalField(max_digits=9,decimal_places=2)
    refId = serializers.CharField()