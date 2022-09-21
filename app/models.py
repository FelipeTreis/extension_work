from django.contrib.auth.models import User
from django.db import models


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
        max_length=7, null=False, blank=False
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
    next_date = models.DateField()
    is_finished = models.BooleanField(default=False)

    @property
    def new_maintenance(self):
        return self.date - self.next_date

    def __str__(self):
        return self.owner
