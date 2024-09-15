from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm #importa um formulario de django
from django.contrib.auth.forms import AuthenticationForm #importa a autenticação de django
from django.contrib.auth import login, logout

# Create your views here.
# redirect, if successfully save the user the redirect back to the post
# a URL conecta a view que liga: template + http + interações 

def register_view(request):
    if request.method == "POST": #se o formulario for submitted
        form = UserCreationForm(request.POST) #formulario é igual ao request post (informaçoes do formulario)
        if form.is_valid(): #função do django pra validar algo
            login(request, form.save()) #se verdade, realiza o login do usuario presente na variavel form.save()
            return redirect("posts:list") # redireciona para posts: name of the app + nome da referencia(localizado na url do projeto)
    else:
        form = UserCreationForm() #aparece o formulario vazio novamente

    template = 'users/register.html'
    return render(request, template, {'form': form})

def login_view(request):
    if request.method == "POST": #se o request do form com o method POST 
        form = AuthenticationForm(data=request.POST) #key word DATA 
        if form.is_valid(): #se a autenticação for valida entao é redirecionado
            login(request, form.get_user())
            return redirect("posts:list")
    else:
        form = AuthenticationForm() #solitica autenticação do formulario
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")