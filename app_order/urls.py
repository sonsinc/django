from django.urls import path
from app_order import views

urlpatterns = [
    path('order', views.order),
    path('history', views.history),
    path('order/<int:order_id>' , views.orderDetail, name='orderDetail'),
]
