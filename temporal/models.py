from django.db import models

# Create your models here.

class Modelo_1(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        abstract: True
        
class Modelo_2(Modelo_1):
    edad = models.IntegerField()
    
    def __str_(self):
        return self.edad 
    