from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from post.models import Post
# Create your views here.

class HomeView(ListView):
  model = Post
  template_name = 'index.html'
  context_object_name= 'posts'

@login_required() # protecing for unauthenticated users
def protected(request):
  return render(request, 'protected.html')
