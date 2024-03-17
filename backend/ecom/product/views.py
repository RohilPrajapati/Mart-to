from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductCreateSerializer,ProductModelSerializer
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from datetime import datetime
from ecom.tokens import decode_token
from users.models import User
from ecom.paginations import PagePaginationCustom
from django.shortcuts import get_object_or_404,get_list_or_404
from ecom.permissions import IsAdminUserOrReadOnly


class ProductListView(APIView,PagePaginationCustom):
    permission_classes = [IsAdminUserOrReadOnly]
    def get(self,request):
        product = Product.objects.all()
        search = request.GET.get('search')
        status = request.GET.get('status')
        if status is not None:
            if status == 't':
                product = product.filter(status=True)
            else:
                product = product.filter(status=False)
        if search is not None:
            product = product.filter(name__icontains=search) | \
                product.filter(description__icontains=search)
        data = self.paginate_queryset(product, request)
        serializer = ProductModelSerializer(data, many=True)
        return self.get_paginated_response(serializer.data)
        
    # permission_classes=[IsAdminUser]
    def post(self,request):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            product = Product.objects.create(name=serializer.validated_data['name'],description = serializer.validated_data['description'],image = serializer.validated_data['image'],stock=serializer.validated_data['stock'],price= serializer.validated_data['price'],status = serializer.validated_data.get('status',True),entry_date=datetime.now(),created_by=User.objects.get(user_id=decode_token(request)['user_id'])    )
            response = {
                'message':'Product have added',
                'data': ProductModelSerializer(product).data
            }
            return Response(response,status=status.HTTP_201_CREATED)

class ProductDetailView(APIView):
    permission_classes = [IsAdminUserOrReadOnly]
    def get(self,request,pk):
        product = get_object_or_404(Product, id=pk)
        response = {
            'data':ProductModelSerializer(product).data
        }
        return Response(response,status=status.HTTP_200_OK)
    
    # permission_classes=[IsAdminUser]
    def put(self,request,pk):
        serializer = ProductCreateSerializer(data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            product = get_object_or_404(Product, id=pk)
            product.name = serializer.validated_data.get('name',product.name)
            # print(serializer.validated_data)
            product.description = serializer.validated_data.get('description',product.description)
            product.image =serializer.validated_data.get('image',product.image)
            product.price = serializer.validated_data.get('price',product.price)
            product.status = serializer.validated_data.get('status',product.status)
            product.stock = serializer.validated_data.get('stock',product.stock)
            product.update_date = datetime.now()
            product.update_by = User.objects.get(user_id=decode_token(request)['user_id'])
            product.save()
            response = {
                'data' : ProductModelSerializer(product).data
            }
            return Response(response,status=status.HTTP_200_OK)

    def patch(self,request,pk):
        obj = get_object_or_404(Product, id=pk)
        if obj.status == True:
            obj.status = False
        else: 
            obj.status = True
        obj.save()
        response = {
            'message':'Status of Product have been updated'
        }
        return Response(response, status=status.HTTP_200_OK)