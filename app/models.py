from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from app.choices import VEHICLE_TYPE_CHOICES


def expiration():
    return now() + timedelta(days=180)


class Brand(models.Model):
    name = models.CharField(
        max_length=255, null=False, blank=False
    )
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AutoModel(models.Model):
    name = models.CharField(
        max_length=255, null=False, blank=False
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE
    )
    type = models.CharField(
        max_length=10, choices=VEHICLE_TYPE_CHOICES,
        default='', null=False, blank=False
    )
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE
    )
    model = models.ForeignKey(
        AutoModel, on_delete=models.CASCADE
    )
    manufacture_year = models.DateField()
    license_plate = models.CharField(
        max_length=7, null=False, blank=False,
        unique=True
    )
    is_active = models.BooleanField(default=False)

    @property
    def vehicle(self):
        return f'{self.owner} - {self.model}'

    def __str__(self):
        return self.vehicle


class Service(models.Model):
    name = models.CharField(
        max_length=255, null=False, blank=False
    )
    value = models.IntegerField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Maintenance(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE
    )
    service = models.ManyToManyField(Service)
    km_vehicle = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    next_date = models.DateField(default=expiration, auto_created=True)
    is_started = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)

    @property
    def full_value(self):
        services = self.service.all()
        value = 0
        for service in services:
            value += service.value
        return value
