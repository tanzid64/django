from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
  return render(request, 'index.html')

@login_required() # protecing for unauthenticated users
def protected(request):
  return render(request, 'protected.html')