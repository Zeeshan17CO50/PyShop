from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def front(request):
    return render(request, 'front.html')


@login_required(login_url='login')
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


@login_required(login_url='login')
def new(request):
    return HttpResponse('New Products')
