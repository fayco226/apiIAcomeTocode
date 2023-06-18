from django.db import models

# Create your models here.
class Appels(models.Model):

    phoneAccountId = models.BigIntegerField()
    number = models.IntegerField()
    callType = models.CharField( max_length=100)
    timestamp = models.BigIntegerField()
    duration = models.IntegerField()
    simDisplayName = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    cachedMatchedNumber = models.CharField( max_length=50)
    cachedNumberType = models.IntegerField()
    
