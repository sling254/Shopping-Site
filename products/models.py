from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=45)
    price = models.FloatField(max_length=100)
    stock = models.CharField(max_length=100)
    supplier_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

