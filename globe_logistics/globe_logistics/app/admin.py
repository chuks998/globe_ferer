from django.contrib import admin
from .models import Shipment

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('tracking_code', 'receiver', 'origin', 'destination', 'status', 'expected_delivery')
    search_fields = ('tracking_code', 'receiver', 'sender', 'origin', 'destination')
    list_filter = ('status', 'shipped_on', 'expected_delivery')
