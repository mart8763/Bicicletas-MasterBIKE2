from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from .models import Product, Customer, Carro
from django.db.models import Count
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.

def index(request):
    """context: paquete variables que pueden ser consumidas por el front"""
    context = {}
    return render(request, "pages/index.html", context)

def index2(request):
    ubicacion = Customer.objects.all()
    context = {'ubicacion':ubicacion}
    return render(request, 'pages/index2.html', context)

def productos(request):
    context = {}
    return render(request, "pages/productos.html",context)

def categoria(request):
    context = {}
    return render(request, "pages/categoria.html", context)

def carro(request):
    context = {}
    return render(request, "pages/carro.html", context)

def registro(request):
    context = {}
    return render(request, "pages/registro.html", context)

def iniciar_sesion(request):
    context = {}
    return render(request, "pages/iniciar_sesion.html", context)

def termino_y_condiciones(request):
    context = {}
    return render(request, "pages/termino_y_condiciones.html", context)

def electrica(request):
    context = {}
    return render(request, "pages/electrica.html", context)

def mtb(request):
    context = {}
    return render(request, "pages/mtb.html", context)

def nino(request):
    context = {}
    return render(request, "pages/nino.html", context)

def ruta(request):
    context = {}
    return render(request, "pages/ruta.html", context)

def urbex(request):
    context = {}
    return render(request, "pages/urbex.html", context)

def compra_realizada(request):
    context = {}
    return render(request, "pages/compra_realizada.html", context)


class CategoriaView(View):
    def get(self, request):
        product = Product.objects.all()
        title = Product.objects.all().values('title')
        return render(request, 'pages/categoria2.html', locals())

class CategoryTitle(View):
    def get(self,request):
        product = Product.objects.all()
        title = Product.objects.all().values('title')
        return render(request, 'pages/categoria2.html', locals())

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'pages/productdetail.html', locals())

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, "pages/customerrestration.html", locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado correctamente")
        else:
            messages.warning(request, "Datos no validos")
            return render(request, "pages/customerrestration.html", locals())
        
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, "pages/profile.html", locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            nombre = form.cleaned_data['nombre']
            direccion = form.cleaned_data['direccion']
            comuna = form.cleaned_data['comuna']
            telefono = form.cleaned_data['telefono']
            region = form.cleaned_data['region']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, nombre=nombre, direccion=direccion, comuna=comuna, telefono=telefono, region=region, zipcode=zipcode)
            reg.save()
            messages.success(request, "Perfil guardado correctamente")
        else:
            messages.warning(request, "Faltaron datos")
        return render(request, "pages/profile.html", locals())
    
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'pages/address.html', locals())

def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id[0])
    Carro(user=user, product=product).save()
    return redirect("/cart")

def show_cart(request):
    user = request.user
    cart = Carro.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.cantidad * p.product.price
        amount = amount + value
    totalcantidad = amount 
    return render(request, 'pages/addtocart.html', locals())

class checkout(View):
    def get(self,request):
        user=request.user
        add=Customer.objects.filter(user=user)
        carro_item = Carro.objects.filter(user=user)
        famount = 0
        for p in carro_item:
            value = p.cantidad * p.product.price
            famount = famount + value
        totalcantidad = famount 
        return render(request, 'pages/checkout.html', locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Carro.objects.get(Q(Product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        user = request.user
        carro = Carro.objects.filter(user=user)
        amount = 0
        for p in carro:
            value = p.cantidad * p.product.price
            amount = amount + value
        totalcantidad = amount 
        data={
            'cantidad':c.cantidad,
            'amount':amount,
            'totalcantidad':totalcantidad
        }
        return JsonResponse(data)
    
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Carro.objects.get(Q(Product=prod_id) & Q(user=request.user))
        c.delete()
        user = request.user
        carro = Carro.objects.filter(user=user)
        amount = 0
        for p in carro:
            value = p.cantidad * p.product.price
            amount = amount + value
        totalcantidad = amount 
        data={
            'amount':amount,
            'totalcantidad':totalcantidad
        }
        return JsonResponse(data)
