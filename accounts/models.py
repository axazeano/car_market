__author__ = 'vladimir'

from django.db import models
from django.contrib.auth.models import User

"""
 All models must have __unicode__() method for properly representation!
"""


class AccountsType(models.Model):
    type = models.CharField(max_length=1, null=False, blank=False, unique=True, primary_key=True)
    description = models.CharField(max_length=100, null=True, blank=True)


    def __unicode__(self):
        return self.type + ' (' + self.description + ')'


class Account(models.Model):
    user = models.ForeignKey(User)
    type = models.ForeignKey('AccountsType', to_field='type')
    balance = models.FloatField(null=False, blank=False)
    is_fully_created = models.BooleanField(null=False, blank=False, default=False)

    def __unicode__(self):
        return self.user.get_full_name() + ' ' + self.type.__unicode__() + ' #' + str(self.pk)

    @staticmethod
    def get_all_accounts_of_user(user):
        return Account.objects.filter(user=user)


class Worker(models.Model):
    name = models.CharField(max_length=120, default='')
    surname = models.CharField(max_length=200, default='')
    salary = models.FloatField(default=0, null=False, blank=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    department = models.CharField(max_length=120, default='')
    owner = models.ForeignKey(Account)

    @staticmethod
    def create_many_workers(account, count, salary=0, is_active=True):
        for x in xrange(count):
            worker = Worker(owner=account,
                            salary=salary,
                            is_active=is_active)
            worker.save()