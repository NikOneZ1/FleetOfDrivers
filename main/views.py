from rest_framework import generics
from .serializers import DriverSerializer
from .models import Driver, Vehicle


class DriversList(generics.ListAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
