from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def product_detail(request):
    return render(request, 'product.html')

def category_page(request):
    return render(request, 'category.html')

def cart_page(request):
    return render(request, 'cart.html')


# Create your views here.
