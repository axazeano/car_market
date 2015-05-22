from django.db import models

from accounts.models import AbstractAccount
from utils.models import Country

class Fabric(AbstractAccount):
    best = models.BooleanField(default=False, null=False, blank=False)
    is_moneyback = models.BooleanField(default=False, null=False, blank=False)



