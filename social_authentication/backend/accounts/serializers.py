import token
from tokenize import TokenError
from urllib import request
from rest_framework import serializers
from accounts.models import User
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_str, force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from accounts.utils import send_normal_email
from rest_framework_simplejwt.tokens import RefreshToken, Token

class UserRegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(max_length=68, min_length=6, write_only=True)
  password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)
  class Meta:
    model = User
    fields = ("email", "first_name", "last_name", "password", "password2")

  def validate(self, attrs):
    password = attrs.get("password", "")
    password2 = attrs.get("password2", "")
    if password != password2:
      raise serializers.ValidationError("Passwords don't match.")
    return attrs
  
  def create(self, validated_data):
    user = User.objects.create_user(
      email = validated_data['email'],
      first_name = validated_data['first_name'],
      last_name = validated_data['last_name'],
      password = validated_data['password']
    )
    return user
  
class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255, min_length=6)
  password = serializers.CharField(max_length=68, write_only=True)
  full_name = serializers.CharField(max_length=255, read_only=True)
  access_token = serializers.CharField(read_only=True)
  refresh_token = serializers.CharField(read_only=True)

  class Meta:
      model = User
      fields = ['email', 'password', 'full_name', 'access_token', 'refresh_token']

  def validate(self, attrs):
    email = attrs.get("email")
    password = attrs.get("password")
    request = self.context.get('request')
    user = authenticate(request, email=email, password=password)
    if not user:
      raise AuthenticationFailed("Invalid credentials, please try again")
    if not user.is_verified:
      raise AuthenticationFailed("Email is not verified")
    user_tokens = user.tokens()
    return {
      'email': user.email,
      'full_name': user.get_full_name,
      'access_token': user_tokens.get('access'),
      'refresh_token': user_tokens.get('refresh')
    }
  
class PasswordRequestSerializer(serializers.Serializer):
  email = serializers.EmailField(max_length=255, min_length=6)
  def validate(self, attrs):
    email = attrs.get('email')
    if User.objects.filter(email=email).exists:
      user = User.objects.get(email=email)
      uidb64 = urlsafe_base64_encode(force_bytes(user.id))
      token = PasswordResetTokenGenerator().make_token(user)
      request = self.context.get("request")
      site_domain = get_current_site(request).domain
      relative_link = reverse('password-reset-confirm-api', kwargs={'uidb64': uidb64, 'token': token})
      abslink = f"http://localhost:5173/password-reset-confirm/{uidb64}/{token}"
      email_body = f"Hi, use the link to reset your password \n {abslink}"
      email_data = {
        'body': email_body,
        'subject': "Reset your password",
        'to': user.email
      }
      send_normal_email(data=email_data)

    return attrs

class SetNewPasswordSerializer(serializers.Serializer):
  password2 = serializers.CharField(max_length=68, min_length=6, write_only=True)
  password = serializers.CharField(max_length=68, min_length=6,write_only=True)
  uidb64 = serializers.CharField(write_only=True)
  token = serializers.CharField(write_only=True)
  
  def validate(self, attrs):
    try:
        password = attrs.get("password")
        password2 = attrs.get("password2")
        uidb64 = attrs.get("uidb64")
        token = attrs.get("token")
        user_id = urlsafe_base64_decode(uidb64)
        user = User.objects.get(id=user_id)
        token_generator = PasswordResetTokenGenerator()
        if not token_generator.check_token(user, token):
          raise AuthenticationFailed("Reset link is invalid or has expired", 401)
        if password != password2:
          raise AuthenticationFailed("Passwords don't match.")
        user.set_password(password)
        user.save()
        return attrs
    except Exception as e:
      raise AuthenticationFailed("Link is invalid or has expired.")
        
class LogoutUserSerializer(serializers.Serializer):
  refresh_token = serializers.CharField()
  default_error_messages = {
    'bad_token': ("Token is Invalid or has expired.")
  }
  def validate(self, attrs):
    self.token = attrs.get('refresh_token')
    return attrs
  
  def save(self, **kwargs):
    try:
      token = RefreshToken(self.token)
      token.blacklist()
    except TokenError:
      return self.fail("bad_token")
    return


