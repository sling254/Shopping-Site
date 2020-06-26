from django.db import models

# Create your models here.


class Supplier(models.Model):
    address = models.CharField(max_length=12)
    phone = models.CharField(max_length=13)
    name = models.CharField(max_length=20)

    
    def __str__(self):
        return self.name


​
