from django.db import models


class Alpha(models.Model):
    version1 = models.CharField(max_length=10)
    version2 = models.PositiveIntegerField()
