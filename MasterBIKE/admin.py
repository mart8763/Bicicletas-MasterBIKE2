from django.contrib import admin
from .models import Customer, Product, Carro,OrderPlaced

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

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','cantidad','orderred_date','status']