from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from .models import Product, Customer, User

# Create your views here.

def index(request):
    """context: paquete variables que pueden ser consumidas por el front"""
    context = {}
    return render(request, "pages/index.html", context)

class productos(View):
    def get(self,request):
        product = Product.objects.all()
        return render(request, "pages/productos.html",locals())

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

def zprueba_usuario(request):
    user = User.objects.all()
    context = {'Usuario':user}
    return render(request, 'pages/zprueba_usuario.html', context)

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
