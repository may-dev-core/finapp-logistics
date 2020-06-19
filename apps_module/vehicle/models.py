from django.db import models
from django.contrib.auth.models import User
from apps_module.company.models import CompanyProfile
from apps_module.apps_settings.models import (
    VehiclePurpose, VehicleType, VehicleFuelType, VehicleStatus)

# Create your models here.


class Vehicle(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    vehicle_code = models.CharField(
        max_length=100, null=True, blank=True)
    vehicle_registration_no = models.CharField(
        max_length=20, unique=True, null=False, blank=False)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_manufacturer = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=20)
    vehicle_color = models.CharField(max_length=20)
    vehicle_fuel_type = models.ForeignKey(
        VehicleFuelType, on_delete=models.CASCADE)
    vehicle_purpose = models.ForeignKey(VehiclePurpose, on_delete=models.CASCADE)

    # vehicle_image = models.CharField(max_length=20, blank=True, null=True)
    vehicle_status = models.ForeignKey(VehicleStatus, on_delete=models.CASCADE)
    vehicle_passenger_limit = models.IntegerField()
    vehicle_cargo_limit = models.IntegerField(help_text="weight in kg")
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.vehicle_registration_no)
