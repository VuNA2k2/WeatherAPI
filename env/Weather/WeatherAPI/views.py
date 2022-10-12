from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, response, status
from rest_framework.views import APIView
from .serializers import UserSerializer, GroupSerializer, GetLocationSerializer, PostLocationSerializer

from .models import Location
from django.shortcuts import render
from rest_framework.response import Response
from .models import WeatherAPI
from .serializers import GetAllWeattherAPISerializer, WeatherAPISerializer

# Create your views here.
class GetAllWeatherAPI(APIView):
    def get(self, request):
        list_weather=WeatherAPI.objects.all()
        mydata=GetAllWeattherAPISerializer(list_weather, many=True)
        return Response(data=mydata.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        mydata=WeatherAPISerializer(data=request.data)
        if  not mydata.is_valid():
            return Response('Sai du lieu',status=status.HTTP_400_BAD_REQUEST)
        Temperature=mydata.data['Temperature1']
        Windspeed=mydata.data['Windspeed1']
        TrangThai=mydata.data['TrangThai1']
        Id=mydata.data['Id1']
        LocationId=mydata.data['LocationId1']
        Date=mydata.data['Date1']
        wt=WeatherAPI.objects.create(Temperature=Temperature,Windspeed=Windspeed,
        TrangThai=TrangThai,Id=Id,LocationId=LocationId,Date=Date)
        return Response(data=wt.id,status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

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
    def put(self, request):
        location = Location.objects.get(id=request.query_params["id"])
        data = PostLocationSerializer(data=request.data)
        if not data.is_valid():
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        location.city = data.data['city']
        location.country = data.data['country']
        location.save()
        return response.Response(data=GetLocationSerializer(location, many=False).data, status=status.HTTP_202_ACCEPTED)

class DeleteLocationAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]
    def delete(self, request):
        location = Location.objects.get(id=request.query_params["id"])
        location.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


