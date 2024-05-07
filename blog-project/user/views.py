from django.shortcuts import redirect
from django.urls import reverse_lazy
from user.forms import UserRegistrationForm
from user.models import User
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.
class UserRegistrationView(CreateView):
  form_class = UserRegistrationForm
  model = User
  success_url = '/'
  template_name = 'registration.html'


class UserLoginView(LoginView):
  template_name = 'login.html'
  fields = "__all__"
  redirect_authenticated_user = False
  def get_success_url(self) -> str:
    return reverse_lazy('index')
  
def UserLogoutView(request):
  logout(request)
  messages.warning(request, 'You have been logged out')
  return redirect('login')