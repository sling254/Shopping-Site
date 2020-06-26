from django.db import models

# Create your models here.

class Order(models.Model):
    deliverystatus = models.CharField(max_length=12)
    quantity = models.CharField(max_length=10)
    orderdate = models.DateField(auto_now_add=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    courrier_id = models.ForeignKey(Courrier, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.deliverystatus


