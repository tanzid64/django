from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import CustomUserManager
# Create your models here.

# Making an abstract model to track created time and updated time
class TimeStampMixin(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True

# Making Custom User Model as default user model
"""
Django provides two types of abstract user model. AbstractUser model basically includes the all fields that we know in django built in user model. On the other hand AbstractBaseUser is used to make a user model from the scratch. You have to implement every single field manually in AbstractBaseUser.
"""
class CustomUser(TimeStampMixin, AbstractUser):
  """
  Fields of AbstractUser: id, password, last_login, is_superuser, username (Special, Unique Constraint), first_name, last_name, email (Special), is_staff, is_active, date_joined
  """
  # My custom fields
  email = models.EmailField(unique=True)
  #... add more as per your need

  objects = CustomUserManager
  USERNAME_FIELD = 'email' # It declears that we will use email while login instad of username
  REQUIRED_FIELDS = ('username',) # An username must required while registration

  def __str__(self) -> str:
    return self.username
