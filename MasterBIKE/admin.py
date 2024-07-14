from django.contrib import admin
from .models import Customer, Product, Carro

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'direccion', 'comuna', 'region', 'zipcode']

@admin.register(Carro)
class CarroModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'cantidad']