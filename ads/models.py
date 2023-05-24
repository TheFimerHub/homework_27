from django.db import models

class Ads(models.Model):
    author = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=10000)
    address = models.CharField(max_length=2000)
    is_published = models.BooleanField(default=False)