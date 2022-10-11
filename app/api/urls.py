from app.api import viewsets
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

app_name = 'api'

router = SimpleRouter()
router.register('users', viewsets.UserViewSet, basename='users')
router.register('brands', viewsets.BrandViewSet, basename='brands')
router.register('automodels', viewsets.AutoModelViewSet, basename='automodel')
router.register('vehicles', viewsets.VehicleViewSet, basename='vehicles')
router.register('services', viewsets.ServiceViewSet, basename='services')
router.register('maintenance', viewsets.MaintenanceViewSet, basename='maintenance')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
]
