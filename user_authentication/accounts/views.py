from django.shortcuts import render
from accounts.models import CustomUser
from accounts.serializers import UserRegistrationSerializer, UserDetailsSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class UserViewSets(viewsets.ModelViewSet):
  queryset = CustomUser.objects.all()
  def get_serializer_class(self):
    if self.request.method == "GET":
      return UserDetailsSerializer
    elif self.request.method == "POST":
      return UserRegistrationSerializer
    return UserSerializer
  lookup_field = 'username' # To get or update single user details use username insted of id
