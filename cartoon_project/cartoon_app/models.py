from django.db import models


# Create your models here.
class CARTOON(models.Model):
    cartoon_name = models.CharField(max_length=50)
    season = models.IntegerField()


