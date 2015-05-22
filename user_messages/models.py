from django.db import models
from django.utils.timezone import now
from accounts.models import Account


class Message(models.Model):
    sender = models.ForeignKey(Account, related_name='sender')
    to = models.ForeignKey(Account, related_name='to')
    title = models.CharField(max_length=120, null=True, blank=True, default='Empty title')
    body = models.TextField(null=False, blank=False, default='')
    send_time = models.DateTimeField(null=False, blank=False, default=now)
    read_time = models.DateTimeField(null=True, blank=True)
