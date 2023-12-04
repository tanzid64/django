from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def homepage(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'index.html', {'form': form})
