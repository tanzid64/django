from django.shortcuts import render
from accounts.serializers import UserRegisterSerializer, UserLoginSerializer, PasswordRequestSerializer, SetNewPasswordSerializer, LogoutUserSerializer
from accounts.models import User, OneTimePassword
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from accounts.utils import send_otp_to_user
from rest_framework.permissions import IsAuthenticated
# For password Reset
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
# Create your views here.

class RegisterUserView(GenericAPIView):
  serializer_class = UserRegisterSerializer

  def post(self, request):
    user_data = request.data
    serializer = self.serializer_class(data=user_data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      user = serializer.data
      send_otp_to_user(user['email'])
      return Response({
        'data':user,
        'message':f"hi {user['first_name']} thanks for signing up, a passcode has been sent to your email"
      }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyUserEmail(GenericAPIView):
  def post(self, request):
    otpCode = request.data.get('otp')

    try:
      user_code_obj = OneTimePassword.objects.get(code=otpCode)
      user = user_code_obj.user
      if not user.is_verified:
        user.is_verified = True
        user.save()
        return Response(
          {
            'message': "Account email verified successfully."
          }, status= status.HTTP_200_OK
        )
      return Response(
        {
          "error": "Code is invalid, user already verified."
        }, status=status.HTTP_204_NO_CONTENT
      )
    except OneTimePassword.DoesNotExist:
      return Response(
        {
          "error": "Otp not provided."
        }, status=status.HTTP_404_NOT_FOUND
      )
    
class LoginUserView(GenericAPIView):
  serializer_class = UserLoginSerializer
  def post(self, request):
    serializer = self.serializer_class(data=request.data, context={'request':request})
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
class PasswordResetRequestView(GenericAPIView):
  serializer_class = PasswordRequestSerializer
  def post(self, request):
    serializer = self.serializer_class(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    return Response(
      {
        'message': "A password reset email has been sent to your email."
      }, status=status.HTTP_200_OK
    )
  
class PasswordResetConfirmView(GenericAPIView):
  def get(self, request, uidb64, token):
    try:
      user_id = urlsafe_base64_decode(uidb64)
      user = User.objects.get(id = user_id)
      token_generator = PasswordResetTokenGenerator()
      if not token_generator.check_token(user, token):
        return Response(
          {
            "error": "Token is invalid"
          }, status=status.HTTP_401_UNAUTHORIZED
        )
      return Response (
        {
          "success": True,
          "message": "Credentials is valid",
          "uidb64": uidb64,
          "token": token
        },status=status.HTTP_200_OK
      )
    except DjangoUnicodeDecodeError:
      return Response(
          {
            "error": "Token is invalid"
          }, status=status.HTTP_401_UNAUTHORIZED
        )
    
class SetNewPasswordView(GenericAPIView):
  serializer_class = SetNewPasswordSerializer
  def patch(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(
      {
        "message": "Password reset successfully"
      }, status=status.HTTP_200_OK
    )

class LogoutUserView(GenericAPIView):
  permission_classes = (IsAuthenticated,)
  serializer_class = LogoutUserSerializer

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(status=status.HTTP_200_OK)