from django.urls import path
from . import views

urlpatterns = [
    path('', views.django_forms, name='home'),
    path('model/', views.django_model, name='model'),
]
