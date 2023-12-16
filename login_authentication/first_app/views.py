from django.shortcuts import render, redirect
from  .import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm 
# Create your views here.
def home(request):
    return render(request, 'home.html')
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('signup')
    else:
        register_form = forms.RegistrationForm()
    
    return render(request, 'signup.html', {'form': register_form, 'type': 'Register'})

def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request,request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login information incorrect')
                return redirect('register')
    else:
        login_form = AuthenticationForm()
        return render(request, 'signup.html', {'form': login_form, 'type': 'Login'})
@login_required
def profile(request):
    return render(request, 'profile.html')
@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserData(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserData(instance=request.user)
        return render(request, 'signup.html', {'form': profile_form, 'type':'Update Profile'})
    
def pass_change(request):
    if request.method == 'POST':
        pass_change_form = PasswordChangeForm( request.user, data = request.POST)
        if pass_change_form.is_valid():
            pass_change_form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, pass_change_form.user)
            return redirect('profile')
    else:
        pass_change_form = PasswordChangeForm(user=request.user)
        return render(request, 'signup.html', {'form': pass_change_form, 'type':'Password Change'})
    
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')