from django.urls import path
from . import views

urlpatterns = [
    path('drivers/driver/', views.DriversList.as_view(), name='drivers_list'),
    path('drivers/driver/<int:pk>', views.GetUpdateDestroyDriver.as_view(), name='driver'),
    path('vehicles/vehicle/', views.VehicleList.as_view(), name='vehicle_list'),
    path('vehicles/vehicle/<int:pk>', views.GetUpdateDestroyVehicle.as_view(), name='vehicle'),
]
