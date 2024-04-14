from django.shortcuts import render
from accounts.models import CustomUser as User
from accounts.permissions import IsOwnerOrReadOnly
from django.contrib.auth import authenticate
from accounts.serializers import UserRegistrationSerializer, UserDetailsSerializer, UserSerializer, UserLoginSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class UserViewSets(viewsets.ModelViewSet):
  permission_classes = [IsOwnerOrReadOnly]
  queryset = User.objects.all()
  def get_serializer_class(self):
    if self.request.method == "GET":
      return UserDetailsSerializer
    elif self.request.method == "POST":
      return UserRegistrationSerializer
    return UserSerializer
  lookup_field = 'username' # To get or update single user details use username insted of id

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(email= email, password=password)
            print(user)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                return Response({'token' : token.key, 'username' : user.username})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)
    
    # {"email": "tanzid@inbox.ru", "password":"123"}
