from django.db import models

# Create your models here.
class TimeStampMixin(models.Model):
  created_at = models.DateTimeField(auto_now_add=True) # Create
  updated_at = models.DateTimeField(auto_now=True) # Edit
  class Meta:
    abstract = True
