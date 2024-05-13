from django.db import models
from django.utils.text import slugify
from core.models import TimeStampMixin
from user.models import User
# Create your models here.

class Post(TimeStampMixin):
  author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
  slug = models.SlugField(unique=True)
  title = models.CharField(max_length=255)
  content = models.TextField()

  def __str__(self):
    return f"{self.title} by {self.author.username}"
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
    super().save(*args, **kwargs)

class Comment(TimeStampMixin):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  content = models.TextField()
