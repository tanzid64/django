from django.shortcuts import render
from accounts.models import CustomUser as User
from accounts.permissions import IsOwnerOrReadOnly
from django.contrib.auth import authenticate
from accounts.serializers import UserRegistrationSerializer, UserDetailsSerializer, UserSerializer, UserLoginSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
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
                return Response({'token' : token.key, 'username' : user.username}, status=status.HTTP_200_OK)
            else:
                return Response({'error' : "Invalid Credential"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)
    
    # {"email": "tanzid@inbox.ru", "password":"123"}
