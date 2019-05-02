# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EventList(models.Model):
    date = models.DateTimeField()
    type = models.ForeignKey('EventType', models.DO_NOTHING, db_column='type')
    channel = models.ForeignKey('EventChannel', models.DO_NOTHING, db_column='channel')
    content = models.CharField(max_length=100)

    def __str__(self) :
        return self.content

    class Meta:
        #managed = False
        db_table = 'event_list'


class EventType(models.Model):
    type = models.CharField(primary_key=True, max_length=45)

    def __str__(self) :
        return self.type

    class Meta:
        #managed = False
        db_table = 'event_type'


class EventChannel(models.Model):
    channel = models.CharField(primary_key=True, max_length=45)

    def __str__(self) :
        return self.channel

    class Meta:
        #managed = False
        db_table = 'event_channel'

class SalesInfoV2(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    product = models.CharField(max_length=45, blank=True, null=True)
    market = models.CharField(max_length=45, blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    is_expired = models.CharField(max_length=1)
    cnt_purchase = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    def __str__(self) :
        return str(self.id)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'sales_info_v2'

class HskCashPurchase(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=40)
    type = models.CharField(max_length=4)
    market = models.CharField(max_length=8)
    price = models.FloatField()
    vat = models.FloatField()
    price_total = models.FloatField()
    is_consumed = models.IntegerField()
    receipt = models.TextField(blank=True, null=True)
    receipt_hash = models.CharField(max_length=255, blank=True, null=True)
    modified_time = models.DateTimeField()
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hsk_cash_purchase'