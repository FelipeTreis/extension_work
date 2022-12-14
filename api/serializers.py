from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import AutoModel, Brand, Maintenance, Service, Vehicle


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
        )


class AutoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoModel
        fields = (
            'id',
            'brand',
            'name',
            'type',
        )

    brand = serializers.CharField()


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            'id',
            'vehicle',
            'brand',
            'manufacture_year',
            'license_plate',
        )

    brand = serializers.CharField()


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            'id',
            'name',
            'value',
        )


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = (
            'id',
            'owner',
            'vehicle',
            'service',
            'full_value',
            'km_vehicle',
            'date',
            'next_date',
        )

    owner = serializers.CharField()
    vehicle = serializers.CharField()
    service = ServiceSerializer(read_only=True, many=True)
    date = serializers.CharField()
    next_date = serializers.CharField()
