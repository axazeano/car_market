from django.db import models
from accounts.models import Account


class Fabric(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    owner = models.ForeignKey('Account')
    balance = models.FloatField(null=False, blank=False, default=500000)


