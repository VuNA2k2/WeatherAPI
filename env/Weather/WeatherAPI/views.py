from os import stat
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics, filters
from rest_framework import permissions, response, status
from rest_framework.views import APIView
from .serializers import GetLocationSerializer, PostLocationSerializer, GetWeatherSerializer, PostWeatherSerializer

from .models import Location, Weather

# Create your views here.

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer



# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

class GetAllLocationAPIView(APIView):

    permission_classes = [ReadOnly]

    def get(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                location = Location.objects.get(id=id)
                data = GetLocationSerializer(location)
        except Location.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except:
            locations = Location.objects.all()
            data = GetLocationSerializer(locations, many=True)
        return response.Response(data=data.data, status=status.HTTP_200_OK)
    
class AddLocationAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        data = PostLocationSerializer(data=request.data)
        if not data.is_valid():
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        location = Location.objects.create(country=data.data['country'], city=data.data['city'])
        return response.Response(data=GetLocationSerializer(location, many=False).data, status=status.HTTP_201_CREATED)
    
class UpdateLocationAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]


    def get(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                location = Location.objects.get(id=id)
                data = GetLocationSerializer(location)
        except Location.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except:
            locations = Location.objects.all()
            data = GetLocationSerializer(locations, many=True)
        return response.Response(data=data.data, status=status.HTTP_200_OK)

    def put(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                location = Location.objects.get(id=id)
                data = PostLocationSerializer(data=request.data)
            if not data.is_valid():
                return response.Response(status=status.HTTP_400_BAD_REQUEST)
            location.country = data.data['country']
            location.city = data.data['city']
            location.save()
            return response.Response(data=GetLocationSerializer(location, many=False).data, status=status.HTTP_202_ACCEPTED)
        except Location.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

class DeleteLocationAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                location = Location.objects.get(id=id)
                data = GetLocationSerializer(location)
        except Location.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except:
            locations = Location.objects.all()
            data = GetLocationSerializer(locations, many=True)
        return response.Response(data=data.data, status=status.HTTP_200_OK)

    def delete(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                location = Location.objects.get(id=id)
            location.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except Location.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

class SearchLocationAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = GetLocationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country', 'city']
    def post(self):
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    # def allowed_methods(self):
    #     return ['GET']

class GetAllWeatherAPIView(APIView):
    permission_classes = [ReadOnly]
    def get(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                weather = Weather.objects.get(id=id)
                data = GetWeatherSerializer(weather)
        except Weather.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except:
            list_weather=Weather.objects.all()
            data=GetWeatherSerializer(list_weather, many=True)
        return response.Response(data=data.data, status=status.HTTP_200_OK)

class AddWeatherAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        data=PostWeatherSerializer(data=request.data)
        if  not data.is_valid():
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        temperature=data.data['temperature']
        wind_speed=data.data['wind_speed']
        status=data.data['status']
        location_id=data.data['location_id']
        date=data.data['date']
        wt=Weather.objects.create(temperature=temperature,wind_speed=wind_speed,
        status=status, location_id=location_id, date=date)
        return response.Response(data=GetWeatherSerializer(wt, many=False).data,status=status.HTTP_200_OK)

class UpdateWeatherAPIView(APIView): 
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                weather = Weather.objects.get(id=id)
                data = GetWeatherSerializer(weather)
        except Weather.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except:
            list_weather=Weather.objects.all()
            data=GetWeatherSerializer(list_weather, many=True)
        return response.Response(data=data.data, status=status.HTTP_200_OK)

    def put(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                weather = Weather.objects.get(id=id)
                data = PostWeatherSerializer(data=request.data)
            if not data.is_valid():
                return response.Response(status=status.HTTP_400_BAD_REQUEST)
            weather.temperature = data.data['temperature']
            weather.wind_speed = data.data['wind_speed']
            weather.status = data.data['status']
            weather.location_id = data.data['location_id']
            weather.date = data.data['date']
            weather.save()
            return response.Response(data=GetWeatherSerializer(weather, many=False).data, status=status.HTTP_202_ACCEPTED)
        except Weather.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
    
class DeleteWeatherAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                weather = Weather.objects.get(id=id)
                data = GetWeatherSerializer(weather)
        except Weather.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        except:
            list_weather=Weather.objects.all()
            data=GetWeatherSerializer(list_weather, many=True)
        return response.Response(data=data.data, status=status.HTTP_200_OK)

    def delete(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                weather = Weather.objects.get(id=id)
            weather.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        except Weather.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

class GetByDateWeatherAPIView(generics.ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = GetWeatherSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['date']

    def post(self):
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)