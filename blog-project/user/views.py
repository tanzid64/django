from django.shortcuts import render
from user.forms import UserRegistrationForm
from user.models import User
from django.views.generic import CreateView
from django.contrib.auth import login,logout



# Create your views here.
class UserRegistrationView(CreateView):
  form_class = UserRegistrationForm
  model = User
  success_url = '/'
  template_name = 'registration.html'
  
  
  