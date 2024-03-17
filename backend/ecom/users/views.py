from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password

from .permissions import IsAdminUser
from ecom.tokens  import decode_token,get_token
from .serializers import UserSerializer, UserLoginSerializer,UserListModelSerializer,ChangePasswordSerializer
from ecom.paginations import PagePaginationCustom
from django.http.response import Http404
from django.db.models import ProtectedError, Q
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from ecom.permissions import IsAdminUserOrReadOnly

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            # checking if the user exist or not
            if not User.objects.filter(email=serializer.validated_data['login_user']).exists():
                if not User.objects.filter(username=serializer.validated_data['login_user']).exists():
                    return Response({'message':"Invalid User"}, status=status.HTTP_401_UNAUTHORIZED)

            # extacting the data
            try:
                user = User.objects.get(email=serializer.validated_data['login_user'])
            except User.DoesNotExist:
                user = User.objects.get(username=serializer.validated_data['login_user'])
            password = serializer.validated_data['password']
            if not user.status:
                return Response({'message':"User is disable"}, status=status.HTTP_401_UNAUTHORIZED)
            # checking if the password is wrong or not
            if not check_password(password, user.password):
                return Response({'message':"Invalid Password"}, status=status.HTTP_401_UNAUTHORIZED)

            # generating the token
            token = get_token(user)
            return Response(token)


class UserRegistration(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save(serializer.validated_data['role_id'],serializer.validated_data['email'],serializer.validated_data['password'])
            try:
                User.objects.get(email=serializer.validated_data['username'])
                return Response('Username cannot be an existing email!')
            except User.DoesNotExist:
                pass
            if not User.objects.filter(email=serializer.validated_data['email']).exists():
                if not User.objects.filter(username=serializer.validated_data['username']).exists():
                    password = serializer.validated_data['password']
                    h_password = make_password(password, salt=None, hasher='default')
                    user = User(username=serializer.validated_data['username'],
                                email=serializer.validated_data['email'], password=h_password)
                    user.save()
                    response = {
                        'message': 'User has been register',
                        'data': serializer.data
                    }
                    return Response(response, status=status.HTTP_201_CREATED)
            response = {
                'message': 'User is already register'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserListView(APIView,PagePaginationCustom):
    permission_classes = [IsAdminUser]
    def get(self,request):
        user = User.objects.all()
        search = request.GET.get('search')
        if search is not None:
            user = user.filter(username__icontains=search) | \
                   user.filter(email__icontains=search)
        user = user.order_by('user_id')
        data = self.paginate_queryset(user, request)
        serializer = UserListModelSerializer(data, many=True)
        return self.get_paginated_response(serializer.data)

class UserDetailView(APIView):
    permission_classes = [IsAdminUserOrReadOnly]
    def get(self,request,pk):
        user = get_object_or_404(User,user_id=pk)
        serializer = UserListModelSerializer(user)
        return Response(serializer.data)
    def put(self,request,pk):
        user = get_object_or_404(User,user_id=pk)
        if user.status:
            user.status = False
            user.save()
            response = {
                'message':'User is Disable'
            }
            return Response(response,status=status.HTTP_200_OK)
        user.status = True
        user.save()
        response = {        
            'message':'User is Enable'
        }
        return Response(response,status=status.HTTP_200_OK)
        


class ChangePasswordView(APIView):
    def post(self,request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            # checking if the user exist or not
            user = User.objects.get(user_id= decode_token(request)['user_id'])
            
            # checking if the password is wrong or not
            if not check_password(old_password, user.password):
                return Response("Invalid Password", status=status.HTTP_409_CONFLICT)
            h_password = make_password(new_password, salt=None, hasher='default')
            user.password = h_password
            user.save()

            response = {
                'message':'Password have been change'
            }
            return Response(response,status = status.HTTP_201_CREATED)