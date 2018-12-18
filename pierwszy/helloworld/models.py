from django.db import models

# Create your models here.
class Math(models.Model):
    function = models.CharField(max_length=3)
    param1 = models.IntegerField()
    param2 = models.IntegerField()