from django import forms
from django.forms.widgets import NumberInput

FAVORITE_COLOR_LIST = [
        ('blue','Blue'),
        ('black', 'Black'),
        ('white', 'White'),
    ]
class contactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Tanzid Haque'})
    )
    roll = forms.IntegerField(
        help_text='Enter six digit roll number'
    )
    email = forms.EmailField(
        label='Email Address:'
    )
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    date = forms.DateField(
        required=False,
        widget=NumberInput(attrs={'type': 'date'})
    )
    agree = forms.BooleanField(
        initial=True
    )
    favorite_color = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=FAVORITE_COLOR_LIST
    )
    favorite_color_multiple = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLOR_LIST
    )