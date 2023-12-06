from django.db import models

# Create your models here.
class Musician(models.Model):
    frist_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    instrument_type = models.CharField(max_length=200)

    def __str__(self):
        return self.frist_name + ' ' + self.last_name
    