from django.db import models
from accounts.models import Account

"""
 All models must have __unicode__() method for properly representation!
"""


class Country(models.Model):
    """Description of Countries in system"""
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __unicode__(self):
        return self.name


class CarsMark(models.Model):
    """Description of Cars Marks. It's base for create cars models"""
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __unicode__(self):
        return self.name


class CarsModel(models.Model):
    """Description of Cars Models"""
    mark = models.ForeignKey('CarsMark')
    name = models.CharField(max_length=100, null=False, blank=False)

    def __unicode__(self):
        return self.mark.name + ' ' + self.name


class Warehouse(models.Model):
    """  Description of Warehouses.
         Fabrics, dealers and shops should have warehouse.
         Fields:
            size - initial size of warehouse;
            free - free places for items;
            owner - account of owner;

         Methods:
            override save
     """
    size = models.IntegerField(null=False, blank=False, default=100)
    free = models.IntegerField(null=False, blank=False)
    owner = models.ForeignKey(Account)

    def save(self, *args, **kwargs):
        """
        Custom save method. Set free = size before save new instance.
        """
        self.free = self.size
        super(Warehouse, self).save(*args, **kwargs)

    def __unicode__(self):
        return ' '.join(['account:', str(self.owner.id),
                         'size:', str(self.size), 'free:' + str(self.free)])


class WarehouseItem(models.Model):
    """  Description of items in Warehouses.
         Fabrics, dealers and shops should have warehouse.
         Fields:
            size - initial size of warehouse;
            free - free places for items;
            owner - account of owner;

         Methods:
            override save
     """
    warehouse = models.ForeignKey('Warehouse')
    item = models.ForeignKey('Part')
    count = models.IntegerField(null=False, blank=False, default=1)

    def __unicode__(self):
        return ' '.join(['warehouse_id:', unicode(self.warehouse_id), 'item:',
                         self.item.__unicode__(), 'count:', str(self.count)])

    def save(self, *args, **kwargs):
        # TODO this is bad idea. Should be separated for two or more methods
        """
        Custom save method. Check count of added items.
        If it > free spaces on a warehouse - exception raises.
        If items already exists in the warehouse - append row.
        Else - create new row.
        """
        if self.count > self.warehouse.free:
            raise Exception('Not enough space in warehouse')
        else:
            try:
                exist_item = WarehouseItem.objects.filter(warehouse=self.warehouse_id, item=self.item_id)

                exist_item.update(count=exist_item.count() + self.count)

                self.warehouse.free -= self.count
                self.warehouse.save()
            except WarehouseItem.DoesNotExist:
                super(WarehouseItem, self).save(*args, **kwargs)

                self.warehouse.free -= self.count
                self.warehouse.save()

class PartType(models.Model):
    type = models.CharField(max_length=120, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True, default='')

    def __unicode__(self):
        return self.type + ' ' + self.description


class Part(models.Model):
    type = models.ForeignKey('PartType')
    car_compability = models.ManyToManyField('CarsModel')
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(null=True, blank=True, default='')

    def __unicode__(self):
        return self.type.type + ' ' + self.name