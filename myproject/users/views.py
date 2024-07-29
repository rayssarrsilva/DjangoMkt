from django.shortcuts import render 
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# redirect, if successfully save the user the redirect back to the post

def register_view(request):
    
    form = UserCreationForm()
    return render(request, 'users/register.html')
