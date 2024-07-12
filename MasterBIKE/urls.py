from mysite.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm


urlpatterns = [
    path("", views.index, name="index"),
    path("productos", views.productos, name="productos"),
    path("categoria", views.categoria, name="categoria"),
    path("carro", views.carro, name="carro"),
    path("registro", views.registro, name="registro"),
    path("iniciar_sesion", views.iniciar_sesion, name="iniciar_sesion"),
    path("termino_y_condiciones", views.termino_y_condiciones, name="termino_y_condiciones"),
    path("electrica", views.electrica, name="electrica"),
    path("mtb", views.mtb, name="mtb"),
    path("nino", views.nino, name="nino"),
    path("ruta", views.ruta, name="ruta"),
    path("urbex", views.urbex, name="urbex"),
    path('profile', views.ProfileView.as_view(), name='profile'),

    #autenticacion de login
    path('registration', views.CustomerRegistrationView.as_view(), name="customerrestration"),
    path('account/login', auth_view.LoginView.as_view(template_name='pages/login.html', authentication_form=LoginForm), name='login'),
    path('password-reset', auth_view.PasswordResetView.as_view(template_name='pages/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)