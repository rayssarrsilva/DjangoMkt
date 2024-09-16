from django import forms 
from . import models #importa os models de models (bd)

class CreatePost(forms.ModelForm):
    class Meta: #Variavel reservada
        model = models.Post # define a variavel model = models + nome da classe criada em models
        fields = ['title', 'body', 'slug', 'banner'] #especifica os campos que ficaram disponiveis na lista