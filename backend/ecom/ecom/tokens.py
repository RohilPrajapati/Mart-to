from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .settings import SIMPLE_JWT
import jwt
from random import randrange

# from user.models import ResetToken


def get_token(user):
    refresh = RefreshToken.for_user(user)
    # refresh.access_token['role'] = user.role_id.name
    refresh['admin'] = user.is_superuser
    return {
    'access': str(refresh.access_token),
    'refresh': str(refresh)
    }

def decode_token(request):
    JWT_authenticator = JWTAuthentication()
    response = JWT_authenticator.authenticate(request)
    user , token = response
    payload = jwt.decode(str(token),SIMPLE_JWT['SIGNING_KEY'],SIMPLE_JWT['ALGORITHM'])
    return payload