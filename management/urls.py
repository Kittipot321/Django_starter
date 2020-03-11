"""POS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',manage,name='manage'),
    path('product/<int:product_id>',product_update,name='pup'),
    path('product',add_product,name='addpd'),
    path('product/add',add_to_database,name='adddb'),
    path('product/delete/<int:product_id>/',delete_product,name='del_product'),
    path('edit_type/',edit_type,name='edittype'),
    path('edit_type/<int:type_id>',type_update,name='typeupdate'),
    path('edit_type/add',add_type,name='addtype'),
    path('edit_type/delete/<int:type_id>/',remove_type,name='deltype'),
    path('product/delete/<int:product_id>/',delete_product,name='del_product'),
]
