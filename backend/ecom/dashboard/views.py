from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,AllowAny
from order.models import Payment
from product.models import Product
from users.models import User
from django.db.models import Sum


class DashboardView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        total_sales = Payment.objects.filter(payment_status=True).count()
        total_sales_amt = Payment.objects.filter(payment_status=True).aggregate(total_sales=Sum('total_amt'))['total_sales']
        total_user = User.objects.all().count()
        total_product = Product.objects.all().count()
        response = {
            'total_sales':total_sales,
            'total_sales_amt':total_sales_amt,
            'total_user':total_user,
            'total_product':total_product
        }
        return Response(response,status=status.HTTP_200_OK)
