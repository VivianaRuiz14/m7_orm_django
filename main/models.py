from django.db import models

# Create your models here.

class estudiante(models.Model):
 nombre = models.CharField(max_length=50)
 apellido = models.CharField(max_length=50)
 email = models.EmailField(max_length=50)
 
 class curso(models.Model):
    cod = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=255)
    activo = models.models.BooleanField(default=False)
    