from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserLoginSerializer(serializers.Serializer):
    login_user = serializers.CharField()
    password = serializers.CharField()

class UserListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id','email','username','is_superuser','status']
        depth = 2

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()

    def save(self, role_id, email, password, username):
        h_password = make_password(password, salt=None, hasher='default')
        user = User(username=username, email=email, password=h_password)
        user.save()

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length = 255)
    new_password = serializers.CharField(max_length = 255)