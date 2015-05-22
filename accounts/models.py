from utils.models import Country

__author__ = 'vladimir'

from django.db import models
from django.contrib.auth.models import User


class Worker(models.Model):
    name = models.CharField(max_length=120, default='')
    surname = models.CharField(max_length=200, default='')
    salary = models.FloatField(default=0, null=False, blank=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    department = models.CharField(max_length=120, default='')
    owner = models.ForeignKey(User)

    @staticmethod
    def create_many_workers(user, count, salary=0, is_active=True):
        for x in xrange(count):
            worker = Worker(owner=user,
                            salary=salary,
                            is_active=is_active)
            worker.save()


class AbstractAccount(models.Model):
    owner = models.OneToOneField(User, default='')
    name = models.CharField(max_length=200, unique=True, default='')
    balance = models.FloatField(default=0.0, null=False, blank=False)
    country = models.ForeignKey(Country, default='')

    class Meta:
        abstract = True