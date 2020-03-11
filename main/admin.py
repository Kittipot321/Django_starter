from django.contrib import admin
from django.contrib.auth.models import Permission
from main.models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Order_Products)
admin.site.register(Permission)
admin.site.register(Type)