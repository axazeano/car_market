from django.contrib import admin
from .models import CarsMark, CarsModel, Country, Warehouse, WarehouseItem, Part, PartType

admin.site.register(Country)
admin.site.register(CarsModel)
admin.site.register(CarsMark)
admin.site.register(Warehouse)
admin.site.register(WarehouseItem)
admin.site.register(Part)
admin.site.register(PartType)


