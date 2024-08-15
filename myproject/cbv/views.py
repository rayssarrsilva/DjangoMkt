from typing import Any
from django.shortcuts import render
from datetime import datetime
from cbv.models import Nome
from django.views.generic.base import TemplateView

#from django.views.generic.base import TemplateView

# Create your views here.

def sla(request):
    abc = datetime.today()
    return render(request, 'ex2.html', {'apresentacao': abc})

def Nomes(request):
    bcd = Nome.objects.all()
    return render(request, 'ex2.html', {'Lista_nomes': bcd})


class Ex2View(TemplateView):

    """ template_name é uma variavel ja existente que insere interação com o template desejado """
    template_name = "ex2.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = Nome.objects.get(id=1)
        context['prefixo'] = "Seu nome é "
        context['prefixo2'] = "o segundo nome é "
        context['nome2'] = context['nome'] = Nome.objects.get(id=2)
        return context
    