from django.db.models import Count
from rest_framework.viewsets import ModelViewSet

from cars.models import Car, CarRating
from cars.serializers import CarReadSerializer, CarCreateSerializer, CarCreateRateSerializer, PopularCarsSerializer


class CarAPIView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CarReadSerializer
        return self.serializer_class


class CarRateAPIView(ModelViewSet):
    queryset = CarRating.objects.all()
    serializer_class = CarCreateRateSerializer
    http_method_names = ['post', 'head']


class PopularCarsAPIView(ModelViewSet):
    serializer_class = PopularCarsSerializer
    http_method_names = ['get', 'head']

    def get_queryset(self):
        return Car.objects.annotate(rates_number=Count('ratings')).order_by('-rates_number')
