from django import forms
from user.models import User

class UserRegistrationForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for field in self.fields:
        self.fields[field].widget.attrs.update({
          "class": 'rounded-lg'
        })
  class Meta:
    model = User
    fields = ('email', 'password',  'username')    
