from django.db import models

# Create your models here.
class CarSpecs(models.Model):
    car_model = models.TextField(max_length=200)
    car_year = models.TextField(max_length=200)
    car_type = models.TextField(max_length=200)
    car_bodytype = models.TextField(max_length=200)
    car_engine = models.TextField(max_length=200)
    