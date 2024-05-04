from django.shortcuts import render

# Create your views here.
def index(request):
  i=10
  return render(request, 'index.html', {'i':i})