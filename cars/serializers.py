from rest_framework import serializers

from cars.models import Car, CarRating
from cars.utils import CarValidatorService


class CarReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'avg_rating')


class CarCreateSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        if make := attrs.get('make'):
            model_service = self.get_model_validation_service()
            if not model_service.is_model_exist(make, model=attrs.get('model')):
                raise serializers.ValidationError('Car model does not exist')
        return attrs

    @staticmethod
    def get_model_validation_service():
        return CarValidatorService()

    class Meta:
        model = Car
        fields = ('make', 'model')


class CarCreateRateSerializer(serializers.ModelSerializer):
    car_id = serializers.IntegerField(required=True)
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = CarRating
        fields = ('car_id', 'rating')


class PopularCarsSerializer(serializers.ModelSerializer):
    rates_number = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ('id', 'make', 'model', 'rates_number')

    def get_rates_number(self, obj):
        return obj.rates_number
