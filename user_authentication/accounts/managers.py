from django.contrib.auth.models import BaseUserManager
"""
A Manager is the interface through which database query operations are provided to Django models. At least one Manager exists for every model in a Django application. The way Manager classes work is documented in Making queries; this document specifically touches on model options that customize Manager behavior.
"""
class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self,username, email, password, password2=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username,email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)