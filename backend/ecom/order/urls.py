from django.urls import path
from .views import CreateOrderView,OrderDetailView,PaymentDetailView,UserWiseOrderView
urlpatterns = [
    path('', CreateOrderView.as_view(), name='order'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('user/<int:user_id>/', UserWiseOrderView.as_view(), name='userwise_older'),
    path('payment/verify/', PaymentDetailView.as_view(), name='payment_verify'),
]
