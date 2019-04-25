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
