from mysite.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm


urlpatterns = [
    path("", views.index, name="index"),
    path("index2/", views.index2, name="index2"),
    path("productos", views.productos, name="productos"),
    path("categoria", views.categoria, name="categoria"),
    path("registro", views.registro, name="registro"),
    path("carro", views.carro, name="carro"),
    path("iniciar_sesion", views.iniciar_sesion, name="iniciar_sesion"),
    path("termino_y_condiciones", views.termino_y_condiciones, name="termino_y_condiciones"),
    path("electrica", views.electrica, name="electrica"),
    path("mtb", views.mtb, name="mtb"),
    path("nino", views.nino, name="nino"),
    path("ruta", views.ruta, name="ruta"),
    path("urbex", views.urbex, name="urbex"),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('address', views.address, name='address'),

    #autenticacion de login
    path('registration', views.CustomerRegistrationView.as_view(), name="customerrestration"),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='pages/login.html', authentication_form=LoginForm), name='login'),
    path('password-reset', auth_view.PasswordResetView.as_view(template_name='pages/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('logout', auth_view.LogoutView.as_view(next_page='login'), name="logout"),

    path('categoria2', views.CategoriaView.as_view(), name='categoria2'),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(), name='product-detail'),
    path('add-to-cart', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('checkout', views.checkout.as_view(), name='checkout'),
    #path('orders', views.orders, name='orders')

    path("pluscart", views.plus_cart),
    path("removecart", views.remove_cart),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)