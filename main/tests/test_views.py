from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from ..models import Driver, Vehicle
from ..serializers import DriverSerializer, VehicleSerializer


class ViewTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    def setUp(self):
        self.driver1 = Driver.objects.create(first_name="name1", last_name="lastname1")
        self.driver2 = Driver.objects.create(first_name="name2", last_name="lastname2")
        self.vehicle1 = Vehicle.objects.create(driver_id=self.driver1,
                                               make="make1",
                                               model="model1",
                                               plate_number="AA1111AA")
        self.vehicle2 = Vehicle.objects.create(driver_id=self.driver1,
                                               make="make2",
                                               model="model2",
                                               plate_number="AA2222AA")
        self.vehicle3 = Vehicle.objects.create(driver_id=self.driver2,
                                               make="make3",
                                               model="model3",
                                               plate_number="AA3333AA")
        self.vehicle3 = Vehicle.objects.create(make="make4",
                                               model="model4",
                                               plate_number="AA4444AA")

    def test_get_list_driver(self):
        """
        Get list of drivers
        """
        resp = self.client.get(reverse('drivers_list'))
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        self.assertEqual(resp.data, serializer.data)
