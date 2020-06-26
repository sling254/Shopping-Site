from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name



