from django.shortcuts import render
from .models import Client, Product, Order, Category
from django.core.files.storage import FileSystemStorage
from datetime import datetime, timedelta
from random import choice
# Create your views here.

def home_page(request):
    context = {'title': 'Home'}
    products = Product.objects.all()
    if products:
        small_product_list = []
        for i in range(4):
            current = choice(products)
            small_product_list.append(current)
        context['products'] = small_product_list
    return render(request, 'market_models_app/home.html', context)

def all_products_page(request):
    context = {'title': 'All products'}
    products = Product.objects.all()
    context['products'] = products
    return render(request, 'market_models_app/all_products.html', context)

def product_page(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    context = {'title': product.name,
               'product': product}
    return render(request, 'market_models_app/product_page.html', context)

def categories_page(request):
    categories = Category.objects.all()
    context = {'title': 'Categories',
               'categories': categories}
    return render(request, 'market_models_app/categories_page.html', context)

def category_page(request, category_id):
    category = Category.objects.filter(pk=category_id).first()
    products = category.products.all()
    context = {'title' : category.name,
               'products': products}
    return render(request, 'market_models_app/category_page.html', context)

