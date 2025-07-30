from django.db import models

# Create your models here.

class Nota(models.Model):
    titulo = models.CharField(max_length=200)   

class Meta:
    ordering = ['titulo',]