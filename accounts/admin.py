from django.contrib import admin

from .models import Account, AccountsType, Worker


# Register your models here.

admin.site.register(Account)
admin.site.register(AccountsType)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'surname', 'department', 'salary', 'is_active')