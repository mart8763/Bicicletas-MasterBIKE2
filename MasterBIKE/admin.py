from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'direccion', 'comuna', 'region', 'zipcode']