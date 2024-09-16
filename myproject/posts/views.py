from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms #Chapter12: importa o arquivo forms presente na pasta local

# Create your views here.

def posts_list(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})

@login_required(login_url="/users/login/") #Verifica se o usuario esta logado, se nao estiver redireciona para a url inserida
def post_new(request):
    form = forms.CreatePost() #variavel para ser chamada por 'form': form
    return render(request, 'posts/post_new.html', {'form': form} )