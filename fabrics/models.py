from django.db import models

from accounts.models import Account
from utils.models import Country


class Fabric(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    owner = models.OneToOneField(Account)
    balance = models.FloatField(null=False, blank=False, default=500000)
    country = models.ForeignKey(Country, null=True, blank=True)



