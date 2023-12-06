from django.shortcuts import render, redirect
from . import forms, models
# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.AddMusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')

    musician_form = forms.AddMusicianForm()
    return render(request, 'add_musician.html', {'form': musician_form})

def edit_musician(request, id):
    musician = models.Musician.objects.get(pk = id)
    musician_form = forms.AddMusicianForm(instance=musician)
    if request.method == 'POST':
        musician_form = forms.AddMusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
        
    return render(request, 'edit_musician.html', {'form': musician_form})

def delete_musician(request, id):
    musician = models.Musician.objects.get(pk = id)
    musician.delete()
    return redirect('homepage')