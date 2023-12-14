from django.shortcuts import render, redirect
from . import forms,models
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

# Add Album
@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):
    model = models.Album
    template_name = 'add_album.html'
    success_url = reverse_lazy('profile')
    form_class = forms.AddAlbumForm

    def form_valid(self, form):
        messages.success(self.request, 'Album Added Successfully')
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Add'
        return context

# Edit Album
@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AddAlbumForm
    template_name= 'add_album.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Album Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Update'
        return context
    
    
