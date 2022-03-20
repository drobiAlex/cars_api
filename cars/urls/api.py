from django.urls import path, include
from rest_framework import routers

from cars.views import CarAPIView, CarRateAPIView, PopularCarsAPIView

app_name = 'cars'

router = routers.DefaultRouter()
router.register(r'cars', CarAPIView, basename='cars')
router.register(r'rate', CarRateAPIView, basename='rates')
router.register(r'popular', PopularCarsAPIView, basename='popular')

urlpatterns = [
    path('', include(router.urls)),
]
