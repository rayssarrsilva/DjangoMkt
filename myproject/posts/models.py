from django.db import models
from django.contrib.auth.models import User #importa o usuario 

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None) #relação 1 pra muitos/ on_delete: especificou que caso se o user for deletado, todos os posts dele será deletado também vice-versa
    
    def __str__(self):
        return self.title
