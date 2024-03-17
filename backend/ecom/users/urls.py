from django.urls import path
from .views import LoginView, UserRegistration,UserListView,ChangePasswordView,UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('registration/', UserRegistration.as_view(), name='registration'),
    # third party url
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password/change/', ChangePasswordView.as_view(), name='change_password'),

]
