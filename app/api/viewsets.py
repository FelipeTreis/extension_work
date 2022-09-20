from app.api.serializers import UserSerializer
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
