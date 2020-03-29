from django.db import models

class ProductORM(models.Model):
    reference = models.CharField(max_length=255, unique=True)
    price = models.IntegerField(default=0)
    nb_reserved = models.IntegerField(default=0)
    nb_available = models.IntegerField(default=0)

class CartProcutOrm(models.Model):
    number = models.IntegerField(null=False)
    product = models.ForeignKey(ProductORM, on_delete=models.CASCADE)