from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
# Create your views here.
def django_forms(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            subject = 'Contact'
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'comment': form.cleaned_data['comment'],
                # 'date': form.cleaned_data['date'],
                # 'favorite_color': form.cleaned_data['favorite_color'],
                # 'favorite_color_multiple': form.cleaned_data['favorite_color_multiple'],
            }
            message = '\n'.join(body.values())
            print(message)
    form = contactForm()
    return render(request, 'index.html', {'form': form})