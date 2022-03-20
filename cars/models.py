from django.db import models
from django_extensions.db.models import TimeStampedModel


class Car(TimeStampedModel):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

    @property
    def avg_rating(self):
        return self.ratings.all().aggregate(models.Avg('rating'))['rating__avg']


class CarRating(TimeStampedModel):
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField()
