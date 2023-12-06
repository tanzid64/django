from django import forms
from .models import Album

class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['release_date']