from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Customer


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus ':'True', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    
class CustomerRegistrationForm(UserCreationForm):
    username =  forms.CharField(widget=forms.TextInput(attrs={'autofocus ': 'True', 'class':'form-control'}))
    email =     forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MyPasswordResetForm(PasswordChangeForm):
    pass

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['nombre', 'direccion', 'comuna', 'telefono', 'region', 'zipcode']
        widget = {
            'nombre' :forms.TextInput(attrs={'class':'form-control'}),
            'direccion' :forms.TextInput(attrs={'class':'form-control'}),
            'comuna' :forms.TextInput(attrs={'class':'form-control'}),
            'telefono' :forms.NumberInput(attrs={'class':'form-control'}),
            'region' :forms.Select(attrs={'class':'form-control'}),
            'zipcode' :forms.NumberInput(attrs={'class':'form-control'}),
        }