from django.contrib import admin

from fabrics.models import Fabric


@admin.register(Fabric)
class FabricAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'country', 'balance')
