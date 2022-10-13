
from itertools import permutations
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/locations/', views.GetAllLocationAPIView.as_view()),
    path('api/add_location/', views.AddLocationAPIView.as_view()),
    path('api/update_location/', views.UpdateLocationAPIView.as_view()),
    path('api/delete_location/', views.DeleteLocationAPIView.as_view()),
    path('api/weatherapp/', views.GetAllWeatherAPIView.as_view()),
    path('api/add_weatherapp/', views.AddWeatherAPIView.as_view()),
    path('admin/', admin.site.urls)
    # path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
