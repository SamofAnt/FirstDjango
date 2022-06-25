from django.db import models

class Flat(models.Model):
    address =  models.CharField(max_length=200)
    price = models.BigIntegerField(default=0)
    isRent = models.BooleanField()

    def __str__(self):
        return self.address
