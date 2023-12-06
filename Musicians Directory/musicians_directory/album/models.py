from django.db import models
from musician.models import Musician
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician,on_delete=models.CASCADE)
    release_date = models.DateField(auto_now_add = True, auto_now= False)
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    def __str__(self) -> str:
        return f'{self.name}, {self.release_date}'