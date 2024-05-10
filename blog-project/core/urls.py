from django.urls import path
from core.views import HomeView, protected

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('protected/', protected, name='protected'),
]
