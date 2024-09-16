from django.shortcuts import render, redirect
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
    if request.method == 'POST': 
        form = forms.CreatePost(request.POST, request.FILES) #request.POST: guarda todas os dados enviados pelo cliente no formulário e request.FILES: contém os arquivos enviados pelo formulário, como imagens, PDFs ou outros tipos de arquivo
        if form.is_valid():
            # save with user
            newpost = form.save(commit=False) # cria uma variavel que salva o formulario
            newpost.author = request.user 
            newpost.save() #salva o post + autor que postou 
            return redirect('posts:list')
    else: #se for apenas acesso, ele cria o formulario
        form = forms.CreatePost() #variavel para ser chamada por 'form': form// cria o formulario 
    return render(request, 'posts/post_new.html', {'form': form} )