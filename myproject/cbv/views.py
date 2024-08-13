from typing import Any
from django.shortcuts import render
from datetime import datetime

#from django.views.generic.base import TemplateView

# Create your views here.

def sla(request):
    abc = datetime.today()
    return render(request, 'ex2.html', {'apresentacao': abc})

