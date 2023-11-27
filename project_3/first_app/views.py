from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author': 'Rahim', 'age': 20, 'lst' : ['Python', 'is', 'best'], 'birthday': datetime.datetime.now(),
        'courses': [
        {
            'id': 1,
            'name': 'Python Course',
            'fee': 5000
        },
        {
            'id': 2,
            'name': 'Django Course',
            'fee': 15000
        },
        {
            'id': 3,
            'name': '"C" Course',
            'fee': 1000
        },
    ]}
    return render(request, 'first_app/home.html', d)