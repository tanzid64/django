from django.shortcuts import render
import datetime

# Create your views here.
def about(request):
    my_dict = {
        'value' : 2, # ADD
        'add_slashes': "I'm Jon", # Add Slashes
        'cap_first': 'the name of our country is Bangladesh', # Cap First
        'content_center': 'centered text', # center
        'cut_text': 'I love Django', # Cut
        'today': datetime.datetime.now(), # Date
        'my_list' : [
            {'name': 'Josh', 'age': 19},
            {'name': 'Dave', 'age': 22},
            {'name': 'Joe', 'age': 31},
        ], # DictSort
    }
    return render(request,'about/about.html', my_dict)