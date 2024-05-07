from django.urls import path
from core.views import index, protected

urlpatterns = [
    path('', index, name='index'),
    path('protected/', protected, name='protected'),
]
