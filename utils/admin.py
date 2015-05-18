from django.contrib import admin

from .models import CarsMark, CarsModel, Country, Warehouse, WarehouseItem, Part, PartType, Message, Order


admin.site.register(Country)
admin.site.register(CarsModel)
admin.site.register(CarsMark)
admin.site.register(Warehouse)
admin.site.register(WarehouseItem)
admin.site.register(Part)
admin.site.register(PartType)
# admin.site.register(Message)
# admin.site.register(Order)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'to', 'body', 'time', 'is_unread')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('sender', 'to', 'part', 'count', 'cost', 'additional_cost')



