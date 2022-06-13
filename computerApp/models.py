from django.db import models
from datetime import datetime

# Create your models here.

class Machine(models.Model):

    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
    )
    id = models.AutoField(primary_key=True,editable=False)
    nom= models.CharField(max_length= 10)
    utilisateur=models.CharField(max_length=15) 
    responsable=models.CharField(max_length=15)
    infrastructure=models.CharField(max_length=15)
    maintenanceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')



class Personnelle(models.Model):

    id = models.AutoField(primary_key=True,editable=False)
    nom=models.CharField(max_length=15)
    prenom=models.CharField(max_length=15)
    infrastructure=models.CharField(max_length=1)
    email=models.EmailField()
    num=models.CharField(max_length=15)
    date_entree=models.DateField(default = datetime.now())


class Infrastructure(models.Model):
    
    id = models.AutoField(primary_key=True,editable=False)
    infrastructure= models.CharField(max_length= 1)
    responsable=models.CharField(max_length=15) 
    nb_machine=models.CharField(max_length=12)
    maintenanceDate = models.DateField(default = datetime.now())
    date_creation=models.DateField(default = datetime.now())
