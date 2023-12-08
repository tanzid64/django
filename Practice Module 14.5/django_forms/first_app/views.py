from django.shortcuts import render
from .forms import contactForm
from . import models
from django.http import HttpResponse
# Create your views here.
def django_forms(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            print(form)
    form = contactForm()
    return render(request, 'index.html', {'form': form})

def django_model(request):
    data = models.Student.objects.all()
    return render(request, 'model.html', {'data':data})