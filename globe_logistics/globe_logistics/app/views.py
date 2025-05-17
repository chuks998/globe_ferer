from django.shortcuts import render, get_object_or_404
from .models import Shipment

def index(request):
    return render(request, "index.html")

def tracker(request):
    tracking_code = request.GET.get("trackingCode")  # changed from "code" to "trackingCode"
    shipment = None
    if tracking_code:
        shipment = get_object_or_404(Shipment, tracking_code=tracking_code)
    return render(request, "tracker.html", {"shipment": shipment})
