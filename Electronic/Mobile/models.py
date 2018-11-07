from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from datetime import date



class Mobile(models.Model):
    company=models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    modelno = models.CharField(max_length=50)
    condition=models.PositiveSmallIntegerField(max_length=25, validators=[MinValueValidator(10), MaxValueValidator(10)])
    price=models.FloatField(max_length=20)
    buy=models.DateField(default=date.today())

    def __str__(self):
        return self.company+'-'+self.modelno

