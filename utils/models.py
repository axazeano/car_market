from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.timezone import now

#from accounts.models import Account
from django.contrib.auth.models import User

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
    owner = models.ForeignKey(User)

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
    # incoming_count isn't a DB Field! Using for change size of free space in a warehouse.
    incoming_count = 0

    def __unicode__(self):
        return ' '.join(['warehouse_id:', unicode(self.warehouse_id), 'item:',
                         self.item.__unicode__(), 'count:', str(self.count)])

    def save(self, *args, **kwargs):
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
                exist_item = WarehouseItem.objects.get(item=self.item)
                exist_item.incoming_count = self.count
                exist_item.count += self.count
                super(WarehouseItem, exist_item).save(*args, **kwargs)
            except models.ObjectDoesNotExist:
                self.incoming_count = self.count
                super(WarehouseItem, self).save(*args, **kwargs)


class PartType(models.Model):
    type = models.CharField(max_length=120, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True, default='')

    def __unicode__(self):
        return self.type + ' ' + self.description


class Part(models.Model):
    type = models.ForeignKey('PartType')
    car_compatibility = models.ManyToManyField('CarsModel')
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(null=True, blank=True, default='')

    def __unicode__(self):
        return self.type.type + ' ' + self.name


class OrderStatus(models.Model):
    """
    Order statuses
    For example: Pending, Working for delivery, Cancel, Done e.t.c.
    """
    status = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=100, default='')


class AdditionalCostType(models.Model):
    """
    Additional Cost types
    For example: overhead cost, extra charge e.t.c.
    """
    type = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=100, default='')


@receiver(post_save, sender=WarehouseItem)
def hold_warehouse_space(instance, **kwargs):
    """
    Change size of free space in a warehouse.
    :param instance: WarehouseItem object
    :param kwargs: Don't using
    :return:
    """
    warehouse = instance.warehouse
    warehouse.free -= instance.incoming_count
    warehouse.save()


@receiver(post_delete, sender=WarehouseItem)
def release_warehouse_space(instance, **kwargs):
    """
    Change size of free space after delete WarehouseItem .
    :param instance: WarehouseItem object
    :param kwargs: Don't using
    :return:
    """
    warehouse = instance.warehouse
    warehouse.free += instance.count
    warehouse.save()