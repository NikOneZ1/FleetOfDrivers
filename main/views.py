from rest_framework import generics, mixins
import datetime
import pytz
from .serializers import DriverSerializer, VehicleSerializer
from .models import Driver, Vehicle


class DriversList(generics.ListCreateAPIView):
    """
    POST: Create driver
    GET: Get list of drivers
    """
    serializer_class = DriverSerializer

    def get_queryset(self):
        created_at_gte = self.request.GET.get("created_at__gte", "").split("-")
        created_at_lte = self.request.GET.get("created_at__lte", "").split("-")
        if created_at_gte[0]:
            created_at_gte = datetime.date(int(created_at_gte[2]), int(created_at_gte[1]), int(created_at_gte[0]))
            return Driver.objects.filter(created_at__gte=created_at_gte)
        elif created_at_lte[0]:
            created_at_lte = datetime.date(int(created_at_lte[2]), int(created_at_lte[1]), int(created_at_lte[0]))
            return Driver.objects.filter(created_at__lte=created_at_lte)
        return Driver.objects.all()


class GetUpdateDestroyDriver(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Get information about driver
    UPDATE: Update information about driver
    DELETE: Destroy driver object
    """
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class VehicleList(generics.ListCreateAPIView):
    """
    POST: Create vehicle
    GET: Get list of drivers
    """
    serializer_class = VehicleSerializer

    def get_queryset(self):
        with_drivers = self.request.GET.get("with_drivers", "")
        if with_drivers == "yes":
            return Vehicle.objects.exclude(driver_id=None)
        elif with_drivers == "no":
            return Vehicle.objects.filter(driver_id=None)
        return Vehicle.objects.all()


class GetUpdateDestroyVehicle(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Get information about vehicle
    UPDATE: Update information about vehicle
    DELETE: Destroy vehicle object
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
