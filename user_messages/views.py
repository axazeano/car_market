from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from accounts.models import Account
from user_messages.models import Messages


@login_required
def inbox(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    messages = Messages.objects.values('send_time').filter(to=account).order_by('send_time')