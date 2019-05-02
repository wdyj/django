from django.contrib import admin

# Register your models here.
from .models import EventList, EventType, EventChannel
admin.site.register(EventList)
admin.site.register(EventType)
admin.site.register(EventChannel)