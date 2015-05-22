from django.db import models
from accounts.models import AbstractAccount
from utils.models import CarsModel


class Customer(AbstractAccount):
    cars = models.ManyToManyField(CarsModel, blank=True, default=None)

    def __unicode__(self):
        return 'Customer: ' + self.account.user.get_full_name()