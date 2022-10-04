from django.db import models

# Create your models here.

class Info(models.Model):
    transaction = models.IntegerField()
    date = models.CharField(max_length=8)
    value = models.FloatField(max_length=10)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.CharField(max_length=6)
    owner = models.CharField(max_length=14)
    store = models.CharField(max_length=19) 