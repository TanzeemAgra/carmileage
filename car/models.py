from django.db import models


class carmil(models.Model):
    cylinders=models.IntegerField()
    displacement=models.IntegerField()
    horsepower=models.IntegerField()
    weight=models.IntegerField()
    acceleration=models.IntegerField()
    model_year=models.IntegerField()
    origin=models.IntegerField()
    mpg=models.FloatField()
    
# Create your models here.
