from django.urls import path
from . import views

urlpatterns = [
    path('', views.front, name='front'),
    path('product', views.index, name='index'),
    path('new', views.new),
]
