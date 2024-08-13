from django.urls import path
from . import views

app_name = 'cbv'

urlpatterns = [
    path('horario/', views.sla, name="list"),
]

