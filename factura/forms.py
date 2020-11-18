from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=30, required=True, help_text='Obligatorio')
    apellidos = forms.CharField(max_length=30, required=True, help_text='Obligatorio')
    email = forms.EmailField(max_length=254, help_text=' Obligatorio')

    class Meta:
        model = User
        fields = ('username', 'nombre', 'apellidos', 'email', 'password',)