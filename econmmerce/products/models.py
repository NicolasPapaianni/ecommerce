from unittest.util import _MAX_LENGTH
from django.db import models        # este viene por default

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=40, unique=True)          # hay que poner si o si el max de caracteres ( y str)
    price = models.FloatField()
    description = models.CharField(max_length=200, null=True, blank=True)  # esto me dice que el campo no es obligatorio llenarlo, puede ser nulo o quedar en blanco
    is_active = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now_add= True, null=True, blank=True)          #con el () me dice que se ingrese el valor por default
    stock = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=50)
    

