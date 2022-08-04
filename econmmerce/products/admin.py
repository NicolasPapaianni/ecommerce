from django.contrib import admin
from products.models import Products

# Register your models here.

# admin.site.register(Products)

# otra manera de registra los productos para que se vean en el admministrador

@admin.register(Products)
class Products_admin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'is_active']



