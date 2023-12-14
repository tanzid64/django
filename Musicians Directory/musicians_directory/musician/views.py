from django.shortcuts import render, redirect
from . import forms, models
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
# Add Musician
@method_decorator(login_required, name='dispatch')
class AddMusicianView(CreateView):
    template_name = 'add_musician.html'
    form_class = forms.AddMusicianForm
    success_url = reverse_lazy('add_musician')

    def form_valid(self, form):
        messages.success(self.request, 'Musician Added Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Add'
        return context
    
    
# Edit Musician
@method_decorator(login_required, name='dispatch')
class EditMusicianView(UpdateView):
    model = models.Musician
    form = forms.AddMusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('homepage')
    fields = '__all__'

    def form_valid(self, form):
        messages.success(self.request, 'Musician Profile Updated Successfully.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Edit'
        return context
    
# Delete Musician
@method_decorator(login_required, name='dispatch')
class DeleteMusicianView(DeleteView):
    model = models.Musician
    template_name = 'delete_musician.html'
    success_url = reverse_lazy('profile')