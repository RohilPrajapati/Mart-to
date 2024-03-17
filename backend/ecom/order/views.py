from rest_framework.views import APIView
from ecom.paginations import PagePaginationCustom
from .models import Payment,OrderItem
from .serializers import CombineOrderCreateSerializer,CombineOrderModelSerializer,PaymentPostSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from ecom.tokens import decode_token
from users.models import User
from rest_framework import status
from uuid import uuid4
from product.models import Product
from django.shortcuts import get_object_or_404,get_list_or_404
import requests as req
import xml.etree.ElementTree as ET
from django.db import transaction
from ecom.permissions import IsAdminUserOrReadOnly

class CreateOrderView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request):
        # query string
        cancel_status = request.GET.get('cancel')
        p_status = request.GET.get('p_status')
        d_status = request.GET.get('d_status')
        p_method = request.GET.get('p_method')
        search = request.GET.get('search')

        order = Payment.objects.all()

        if search:
            order = order.filter(username__icontains=search) | \
                order.filter(contact__icontains=search) | \
                    order.filter(address__icontains=search  ) 
            
        if cancel_status == 'True':
            order = order.filter(cancel_status=True)
        elif cancel_status == 'False':
            order= order.filter(cancel_status=False)

        if p_status == 'Paid':
            order = order.filter(payment_status=True)
        elif p_status == 'Unpaid':
            order= order.filter(payment_status=False)
        
        if d_status == 'True':
            order = order.filter(delivery_status=True)
        elif d_status == 'False':
            order= order.filter(delivery_status=False)
        
        if p_method == 'Online':
            order = order.filter(payment_method='online')
        elif p_method == 'Cash':
            order= order.filter(payment_method='cash')
        order = order.order_by('id')
        response = {
            'data':CombineOrderModelSerializer(order,many=True).data
        }
        return Response(response,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = CombineOrderCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                with transaction.atomic():
                    order_items = serializer.validated_data['order_item']
                    total_amt = 0
                    for item in order_items:
                        sub_total =  item['quantity'] * item['price']
                        total_amt += sub_total
                    payment_uid = uuid4()
                    print(payment_uid)
                    payment = Payment.objects.create(order_by = User.objects.get(user_id=decode_token(request)['user_id']), address= serializer.validated_data['address'],contact= serializer.validated_data['contact'], total_amt= total_amt,payment_uid = payment_uid,payment_method = serializer.validated_data['payment_method'],username=serializer.validated_data['username']) 
                    
                    for item in order_items:
                        product = Product.objects.get(id = item['product']) 
                        product.stock = product.stock - item['quantity']
                        if not product.status:
                            raise Exception('Sorry, Product is not avaiable')
                        if product.stock < 0:
                            raise Exception("Order Item is more then stock")
                        order_item = OrderItem.objects.create(quantity=item['quantity'],price= item['price'],product=product,payment=payment)
                        product.save()
                    response = {
                        'data':CombineOrderModelSerializer(payment).data
                    }
                    return Response(response,status=status.HTTP_201_CREATED)
            except Exception as e:
                response = {
                    'message':'{}'.format(e)
                }
                return Response(response,status=status.HTTP_400_BAD_REQUEST)



class OrderDetailView(APIView):
    permission_classes = [IsAdminUserOrReadOnly]
    def get(self,request,pk):
        payment = get_object_or_404(Payment,id=pk)
        response = {
            'data' : CombineOrderModelSerializer(payment).data
        }
        return Response(response,status=status.HTTP_200_OK)
    def put(self,request,pk):
        payment = get_object_or_404(Payment,id=pk)
        if payment.delivery_status == True:
            payment.delivery_status = False
        else:
            payment.delivery_status = True
        payment.save()
        response = {
            'data':CombineOrderModelSerializer(payment).data
        }
        return Response(response,status=status.HTTP_200_OK)

class UserWiseOrderView(APIView):
    def get(self,request,user_id):
        if decode_token(request)['user_id'] != user_id:
            response = {
                'message':'User is not authorized to access this data'
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        payment = get_list_or_404(Payment,order_by = user_id)
        response = {
            'data':CombineOrderModelSerializer(payment,many=True).data
        }
        return Response(response,status=status.HTTP_200_OK)

class PaymentDetailView(APIView):
    def post(self,request):
        serializer = PaymentPostSerializer(data=request.data)
        # saving payment
        if serializer.is_valid(raise_exception=True):
            oid = serializer.validated_data['oid']
            total_amt = serializer.validated_data['amt']
            r_id = serializer.validated_data['refId']
            if not Payment.objects.filter(payment_uid=oid,total_amt = total_amt).exists():
                response = {
                    'message': 'Payment with this Unique id not found'
                }
                return Response(response,status=status.HTTP_400_BAD_REQUEST)
            elif Payment.objects.filter(payment_uid=oid,total_amt = total_amt,payment_status=True).exists():
                response = {
                    'message': 'Payment Already been Done'
                }
                return Response(response,status=status.HTTP_400_BAD_REQUEST)
            
            # validating payment in esewa

            url ="https://uat.esewa.com.np/epay/transrec"
            data = {
                'amt': total_amt,
                'scd': 'EPAYTEST',
                'rid': r_id,
                'pid': oid,
            }
            resp = req.post(url, data)
            root = ET.fromstring(resp.content)
            if root[0].text.strip() == "Success":
                payment = Payment.objects.get(payment_uid = oid)
                payment.transaction_id = r_id
                payment.payment_status= True
                payment.save()
                response = {
                    'message':'Payment Successfull'
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                response = {
                    'message':'Payment Failed'
                }
                return Response(response,status=status.HTTP_200_OK)

