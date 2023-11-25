from django.http import HttpResponse

def home(request):
    return HttpResponse('This is Home Page')
def contact(request):
    return HttpResponse('This is contact Page')