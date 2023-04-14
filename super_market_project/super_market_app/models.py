from django.db import models


class Add(models.Model):
    value_1 = models.IntegerField()
    value_2 = models.IntegerField()

