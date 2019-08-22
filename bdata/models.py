from django.db import models


class BData(models.Model):
    version1 = models.CharField(max_length=10)
    version2 = models.CharField(max_length=10)
    version3 = models.CharField(max_length=10)
    age = models.IntegerField()
