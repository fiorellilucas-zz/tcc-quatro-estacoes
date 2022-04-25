from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

from . import models

class MoradorCreationForm(UserCreationForm):

    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="",
    )
    password2 = forms.CharField(
        label="Confirme sua senha",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="",
    )
    
    class Meta:
        model = models.Morador
        fields = ["email", "first_name", "last_name", "bloco", "apartamento", "interfone", "celular"]
        labels = {
            "first_name": "Nome",
            "last_name": "Sobrenome"
        }



class MoradorChangeForm(ModelForm):

    class Meta:
        model = models.Morador
        fields = ["email","first_name", "last_name", "bloco", "apartamento", "interfone", "celular"]
        labels = {
            "first_name": "Nome",
            "last_name": "Sobrenome"
        }


class ReuniaoForm(ModelForm):
    
    class Meta:
        model = models.Reuniao
        fields = "__all__"
        widgets = {
            "data": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class ReclamacaoForm(ModelForm):

    class Meta:
        model = models.Reclamacao
        fields = "__all__"


class AvisoForm(ModelForm):

    class Meta:
        model = models.Aviso
        fields = "__all__"
        widgets = {
            "data_evento": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class ReservaForm(ModelForm):

    class Meta:
        model = models.Reserva
        fields = ["data"]
        widgets = {
            "data": forms.DateInput(attrs={"type": "date"}),
        }

