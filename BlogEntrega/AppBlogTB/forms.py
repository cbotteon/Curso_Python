from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Escritor, Paper


class EscritorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    documento = forms.IntegerField()
    profesion = forms.CharField()
    email = forms.EmailField()

class PaperFormulario(forms.ModelForm):
    class Meta:
        model = Paper
        fields = "__all__"

    # La clase paper tiene una ForeingKey por eso se usa ModelForm y Meta....

class BuscaEscritorForm(forms.Form):
    apellido = forms.CharField()


# Para poner más estética la vista de registro de usuarios creo este formulario
# Heredo lo del formulario Django (UserCreationForm)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','last_name', 'first_name']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2','last_name', 'first_name']
        help_texts = {k:"" for k in fields}
