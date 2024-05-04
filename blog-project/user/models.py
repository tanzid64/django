from django.db import models
from core.models import TimeStampMixin
from django.contrib.auth.models import AbstractUser
from user.managers import UserManager


class User(TimeStampMixin, AbstractUser):
  phone = models.CharField(max_length=12, null=True, blank=True)
  email = models.EmailField(max_length=255, unique=True)

  objects = UserManager()
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']