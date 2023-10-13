from django.urls import path
from app_gen import views

urlpatterns = [
    path('', views.index),
    path('product/details/<int:id>', views.productDetail, name='productDetail'),
    path('products', views.products),
    path('about', views.about),    
    path('contact', views.contact),


]
