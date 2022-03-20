from django.urls import path, include

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

api_urls = [
    path('', include('cars.urls.api', namespace='cars')),
]

urlpatterns += [
    path('', include((api_urls, 'api'), namespace='api'))
]
