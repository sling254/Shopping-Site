from django.db import models

# Create your models here.

class Courrier (models.Model):
    name = models.CharField(max_length=12)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=12)

    
    def __str__(self):
        return self.name
    

