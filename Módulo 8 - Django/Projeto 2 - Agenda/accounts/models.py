from django.db import models
from contatos.models import Contato
from django import forms


class CadastrarContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('publicar',)
