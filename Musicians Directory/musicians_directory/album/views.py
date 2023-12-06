from django.shortcuts import render, redirect
from . import forms,models
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AddAlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')

    album_form = forms.AddAlbumForm()
    return render(request, 'add_album.html', {'form': album_form})

def edit_album(request, id):
    album = models.Album.objects.get(pk = id)
    album_form = forms.AddAlbumForm(instance=album)
    if request.method == 'POST':
        album_form = forms.AddAlbumForm(request.POST, instance=album)
        if album_form.is_valid():
                album_form.save()
                return redirect('homepage')

    return render(request, 'edit_album.html', {'form': album_form})