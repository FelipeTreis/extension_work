from app.api.serializers import (AutoModelSerializer, BrandSerializer,
                                 MaintenanceSerializer, ServiceSerializer,
                                 UserSerializer, VehicleSerializer)
from app.models import AutoModel, Brand, Maintenance, Service, Vehicle
from decouple import config
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = config('PER_PAGE_VIEWSET', default=10)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    pagination_class = Pagination


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.filter(is_active=True)
    serializer_class = BrandSerializer
    pagination_class = Pagination


class AutoModelViewSet(viewsets.ModelViewSet):
    queryset = AutoModel.objects.filter(is_active=True)
    serializer_class = AutoModelSerializer
    pagination_class = Pagination


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.filter(is_active=True)
    serializer_class = VehicleSerializer
    pagination_class = Pagination


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    pagination_class = Pagination


class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.filter(is_finished=True)
    serializer_class = MaintenanceSerializer
    pagination_class = Pagination
