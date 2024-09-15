from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.

def posts_list(request):
    posts = Post.objects.all().order_by('date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

@login_required(login_url="/users/login/") #Verifica se o usuario esta logado, se nao estiver redireciona para a url inserida
def post_page(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})

def post_new(request):
    return render(request, 'posts/post_new.html')