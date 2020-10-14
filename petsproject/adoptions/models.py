import sqlite3
from django.db import models

# Create your models here.

class Pet(models.Model) :
    #for better display of the information we are taking  
    SEX_CHOICES =[('M','MALE'),('F','FEMALE')]
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100,blank=True)
    description = models.TextField(max_length=100)
    sex = models.CharField(max_length=30,choices=SEX_CHOICES)
    age =models.IntegerField(null=True)
    submission_date=models.DateTimeField()
    vaccinations = models.ManyToManyField('Vaccine',blank=True)  
class Vaccine(models.Model):
    #this vacines.name is declared as vacchination with many to many relationship in other class
    name = models.CharField(max_length=100) 
    #this is a magic method called when object is called , here we are just overriding how our objects description shold be returned or
    def __str__(self):
        return self.name