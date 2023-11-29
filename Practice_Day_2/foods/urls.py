from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_details, name='food-details'),
]
