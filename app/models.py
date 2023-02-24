from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=200)
    relation_ship=models.CharField(max_length=300)
    email=models.EmailField(max_length=255)
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
