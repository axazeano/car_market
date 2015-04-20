__author__ = 'vladimir'

from django.db import models
from django.contrib.auth.models import User

"""
 All models must have __unicode__() method for properly representation!
"""


class AccountsType(models.Model):
    type = models.CharField(max_length=1, null=False, blank=False, unique=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.type + ' (' + self.description + ')'


class Account(models.Model):
    user = models.ForeignKey(User)
    type = models.ForeignKey('AccountsType', to_field='type')
    balance = models.FloatField(null=False, blank=False)

    def __unicode__(self):
        return self.user.get_full_name() + ' ' + self.type.__unicode__()