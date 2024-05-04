from django import forms
from user.models import User

class UserRegistrationForm(forms.ModelForm):

  class Meta:
    model = User
    fields = ('email', 'password',  'username')
    