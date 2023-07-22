from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Product(models.Model):
    grade_list = (
        ['ECONOMY', 'ECONOMY']
        , ['PREMIUM_ECONOMY', 'PREMIUM_ECONOMY']
        , ['BUSINESS', 'BUSINESS']
        , ['FIRST', 'FIRST']

    )

    flystart = models.CharField(max_length=30)
    flyend = models.CharField(max_length=30)
    datefly = models.DateField()



    def __str__(self):
        return self.title


