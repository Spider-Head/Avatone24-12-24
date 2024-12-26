from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product_detail, name='product'),
    path('category/', views.category_page, name='category'),
    path('cart/', views.cart_page, name='cart'),
]
