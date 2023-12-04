from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label = 'username')
    file = forms.FileField()
    # email = forms.EmailField()
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birthDay = forms.DateField()
    # appoinment = forms.DateTimeField()
    # CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # size = forms.ChoiceField(choices=CHOICES)
    # MEAL = [('P','Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    # pizza = forms.MultipleChoiceField(choices=MEAL)