from django.urls import path
from . import views

urlpatterns = [
    path('drivers/driver/', views.DriversList.as_view(), name='drivers_list')
]
