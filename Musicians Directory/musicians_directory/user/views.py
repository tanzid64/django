from typing import Any
from django.db.models.base import Model as Model
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import SignUpForm, ChangeUserForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from album.models import Album
# Create your views here.
# SignUP
class UserSignUpView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        messages.success(self.request, 'Signup Successfull')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Please Enter Valid Information')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['type'] = 'Sign Up as new User'
        return context
# Login
class UserLoginView(LoginView):
    template_name = 'signup.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.danger(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['type'] = 'Log In'
        return context
    
# Profile
@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    template_name = 'profile.html'
    model = User
    def get_object(self):
        return self.request.user
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["data"] = Album.objects.all()
        return context
    

# Edit Profile
@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    model = User
    template_name = 'signup.html'
    form_class = ChangeUserForm
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Profile Updated Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Information Incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update Your Profile'
        return context
    
# Edit Password
@method_decorator(login_required, name='dispatch')
class EditPasswordView(PasswordChangeView):
    template_name = 'signup.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Password Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['type'] = 'Update Your Password'
        return context
    
#LogOut
@method_decorator(login_required, name='dispatch')
class UserLogoutView(LogoutView):
    def get_success_url(self):
        messages.success(self.request, 'Logged out successfully')
        return reverse_lazy('login')

