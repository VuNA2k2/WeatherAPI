
from itertools import permutations
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/login', TokenObtainPairView.as_view(), name='login'),
    path('api/user/register/', views.RegisterUserAPIView.as_view(), name='register'),
    path('api/user/edit_user/', views.EditUserAPIView.as_view(), name='edit'),
    path('api/user/delete_user/', views.DeleteUserAPIView.as_view(), name='delete'),
    path('api/location/get_location/', views.GetAllLocationAPIView.as_view()),
    path('api/location/add_location/', views.AddLocationAPIView.as_view()),
    path('api/location/update_location/', views.UpdateLocationAPIView.as_view()),
    path('api/location/delete_location/', views.DeleteLocationAPIView.as_view()),
    path('api/location/search_location/', views.SearchLocationAPIView.as_view()),
    path('api/weather/get_weather/', views.GetAllWeatherAPIView.as_view()),
    path('api/weather/add_weather/', views.AddWeatherAPIView.as_view()),
    path('api/weather/update_weather/', views.UpdateWeatherAPIView.as_view()),
    path('api/weather/delete_weather/', views.DeleteWeatherAPIView.as_view()),
    path('api/weather/get_weather_by_date/', views.GetWeatherByDateAPIView.as_view()),
    path('api/weather/get_weather_by_location_id/', views.GetWeatherByLocationAPIView.as_view()),
    path('api/weather/get_weather_by_location_at_date/', views.GetWeatherByLocationAtDateAPIView.as_view()),
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
