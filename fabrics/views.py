from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import Account, AccountsType, Worker
from fabrics.models import Fabric
from utils.models import Country, Warehouse, Message


@login_required
def create_fabric(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        return render(request, 'fabrics/create_fabric.html',
                      {'countries': countries})
    if request.method == 'POST':
        data = request.POST
        account = Account(user=request.user,
                          type=AccountsType.objects.get(pk='F'),
                          balance=0)
        account.save()
        fabric = Fabric(name=data['id_name'],
                        owner=account,
                        balance='0',
                        country=Country.objects.get(name=data['id_country']))
        fabric.save()
        warehouse = Warehouse(owner=account,
                              size=int(data['id_warehouse_size']),
                              free=int(data['id_warehouse_size']))
        warehouse.save()
        Worker.create_many_workers(account=account,
                                   count=int(data['id_workers_count']))

        return render(request, 'fabrics/fabric_view.html', {'fabric': fabric,
                                                            'account': account,
                                                            'warehouse': warehouse})


@login_required
def fabric_dashboard(request, account_id):
    if request.method == 'GET':
        account = Account.objects.get(pk=account_id)
        fabric = Fabric.objects.get(owner=account)
        warehouse = Warehouse.objects.get(owner=account)
        workers = Worker.objects.filter(owner=account)
        new_messages_count = Message.objects.filter(to=account, is_unread=True).count()

        context = {'account': account,
                   'fabric': fabric,
                   'warehouse': warehouse,
                   'workers': workers,
                   'new_messages_count': new_messages_count}

        return render(request, 'fabrics/fabric_dashboard.html', context)


@login_required
def fabric_messages(request, account_id):
    if request.method == 'GET':
        account = Account.objects.get(pk=account_id)
        messages = Message.objects.filter(to=account)

        context = {'messages': messages}

        return render(request, 'fabrics/messages.html', context)