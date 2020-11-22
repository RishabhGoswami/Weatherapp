from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.adds,name='adds'),
    path('index',views.index,name='index'),
]