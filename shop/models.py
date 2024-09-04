from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Products(models.Model):

    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.FloatField()
    image = models.CharField(max_length=300)


class Order(models.Model):
    items = models.CharField(max_length = 2000)
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    zipcode = models.CharField(max_length = 200)
    phoneNumber = models.IntegerField()
    total = models.FloatField()