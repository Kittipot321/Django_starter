from django.contrib import admin
from django.contrib.admin import AdminSite
from main.models import Product,Type,Order,Order_Products
# Register your models here.
class AddType(AdminSite):
    site_header = "Add/Edit Type"
    site_title = "Hello"
    index_title = "Add/Edit type"
event_admin_site = AddType(name='event_admin')
event_admin_site.register(Type)
