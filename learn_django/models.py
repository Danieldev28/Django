from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    
    
    def __str__(self):
        return (self.name)
    
class Visitor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=200)
      
    def __str__(self):
        return (self.name)