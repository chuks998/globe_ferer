from django.db import models

# Create your models here.

class Shipment(models.Model):
    STATUS_CHOICES = [
        ('order_placed', 'Order Placed'),
        ('dispatched', 'Dispatched'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    ]

    tracking_code = models.CharField(max_length=32, unique=True)
    sender = models.CharField(max_length=128)
    receiver = models.CharField(max_length=128)
    receiver_image = models.ImageField(upload_to='shipments/', blank=True, null=True)
    origin = models.CharField(max_length=128)
    destination = models.CharField(max_length=128)
    weight = models.CharField(max_length=32)
    shipped_on = models.DateField()
    expected_delivery = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='order_placed')
    # Optionally, add a shipment image
    shipment_image = models.ImageField(upload_to='shipments/', blank=True, null=True)

    def __str__(self):
        return f"{self.tracking_code} - {self.receiver}"
