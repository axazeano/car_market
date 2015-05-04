from django.db import models

from accounts.models import Account
from utils.models import CarsModel


class Customer(models.Model):
    account = models.ForeignKey(Account)
    cars = models.ManyToManyField(CarsModel, blank=True, default=None)

    def __unicode__(self):
        return 'Customer: ' + self.account.user.get_full_name()

    def save(self):
        if self.account.type.type != 'C':
            raise Exception("Account with type {} can't be a customer".format(self.account.type.type))
        else:
            super(Customer, self).save()