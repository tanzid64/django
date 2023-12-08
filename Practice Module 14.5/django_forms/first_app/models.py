from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='')
    adderss = models.TextField()
    s_class = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.id} - {self.name}'