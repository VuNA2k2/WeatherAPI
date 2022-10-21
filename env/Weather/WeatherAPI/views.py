from os import stat
from django.contrib.auth.models import User
from rest_framework import generics, filters
from rest_framework import permissions, response
from rest_framework import status as st
from rest_framework.views import APIView
from .serializers import GetLocationSerializer, PostLocationSerializer, GetWeatherSerializer, PostWeatherSerializer, UserSerializer, EditUserSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Location, Weather


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class GetAllLocationAPIView(APIView):

    permission_classes = [ReadOnly]

    @swagger_auto_schema(
        responses={200: openapi.Response(
            'response description', GetLocationSerializer)},
        manual_parameters=[openapi.Parameter('id', openapi.IN_QUERY, description="Get location by id", type=openapi.TYPE_INTEGER)],)
    def get(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                location = Location.objects.get(id=id)
                data = GetLocationSerializer(location)
        except Location.DoesNotExist:
            return response.Response(status=st.HTTP_404_NOT_FOUND)
        except:
            locations = Location.objects.all()
            data = GetLocationSerializer(locations, many=True)
        return response.Response(data=data.data, status=st.HTTP_200_OK)


class AddLocationAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(request_body=PostLocationSerializer, responses={201: openapi.Response('created', GetLocationSerializer)})
    def post(self, request):
        data = PostLocationSerializer(data=request.data)
        if not data.is_valid():
            return response.Response(status=st.HTTP_400_BAD_REQUEST)
        location = Location.objects.create(
            country=data.data['country'], city=data.data['city'])
        return response.Response(data=GetLocationSerializer(location, many=False).data, status=st.HTTP_201_CREATED)


class UpdateLocationAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        responses={202: openapi.Response(
            'update success', GetLocationSerializer)},
        manual_parameters=[openapi.Parameter(
            'id', openapi.IN_QUERY, description="Update location by id", type=openapi.TYPE_INTEGER)],
        request_body=PostLocationSerializer)
    def put(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                location = Location.objects.get(id=id)
                data = PostLocationSerializer(data=request.data)
            if not data.is_valid():
                return response.Response(status=st.HTTP_400_BAD_REQUEST)
            location.country = data.data['country']
            location.city = data.data['city']
            location.save()
            return response.Response(data=GetLocationSerializer(location, many=False).data, status=st.HTTP_202_ACCEPTED)
        except Location.DoesNotExist:
            return response.Response(status=st.HTTP_404_NOT_FOUND)


class DeleteLocationAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        responses={204: openapi.Response('delete')},
        manual_parameters=[openapi.Parameter('id', openapi.IN_QUERY, description="Delete location by id", type=openapi.TYPE_INTEGER)],)
    def delete(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                location = Location.objects.get(id=id)
                weather = Weather.objects.filter(location_id=id)
                location.delete()
                weather.delete()
                return response.Response(status=st.HTTP_204_NO_CONTENT)
        except Location.DoesNotExist:
            return response.Response(status=st.HTTP_404_NOT_FOUND)


class SearchLocationAPIView(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = GetLocationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country', 'city']


class GetAllWeatherAPIView(APIView):
    permission_classes = [ReadOnly]

    @swagger_auto_schema(
        responses={200: openapi.Response(
            'response description', GetWeatherSerializer)},
        manual_parameters=[openapi.Parameter('id', openapi.IN_QUERY, description="Get weather by id", type=openapi.TYPE_INTEGER)],)
    def get(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                weather = Weather.objects.get(id=id)
                data = GetWeatherSerializer(weather)
        except Weather.DoesNotExist:
            return response.Response(status=st.HTTP_404_NOT_FOUND)
        except:
            list_weather = Weather.objects.all()
            data = GetWeatherSerializer(list_weather, many=True)
        return response.Response(data=data.data, status=st.HTTP_200_OK)


class AddWeatherAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        responses={200: openapi.Response(
            'response description', GetWeatherSerializer)},
        request_body=PostWeatherSerializer)
    def post(self, request):
        data = PostWeatherSerializer(data=request.data)
        if not data.is_valid():
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        temperature = data.data['temperature']
        wind_speed = data.data['wind_speed']
        status = data.data['status']
        location_id = data.data['location_id']
        date = data.data['date']
        wt = Weather.objects.create(temperature=temperature, wind_speed=wind_speed,
                                    status=status, location_id=location_id, date=date)
        return response.Response(data=GetWeatherSerializer(wt, many=False).data, status=st.HTTP_200_OK)


class UpdateWeatherAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        responses={202: openapi.Response(
            'update success', GetWeatherSerializer)},
        manual_parameters=[openapi.Parameter(
            'id', openapi.IN_QUERY, description="Update weather by id", type=openapi.TYPE_INTEGER)],
        request_body=PostWeatherSerializer)
    def put(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                weather = Weather.objects.get(id=id)
                data = PostWeatherSerializer(data=request.data)
            if not data.is_valid():
                return response.Response(status=st.HTTP_400_BAD_REQUEST)
            weather.temperature = data.data['temperature']
            weather.wind_speed = data.data['wind_speed']
            weather.status = data.data['status']
            weather.location_id = data.data['location_id']
            weather.date = data.data['date']
            weather.save()
            return response.Response(data=GetWeatherSerializer(weather, many=False).data, status=st.HTTP_202_ACCEPTED)
        except Weather.DoesNotExist:
            return response.Response(status=st.HTTP_404_NOT_FOUND)


class DeleteWeatherAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(
        responses={204: openapi.Response('delete')},
        manual_parameters=[openapi.Parameter('id', openapi.IN_QUERY, description="Delete weather by id", type=openapi.TYPE_INTEGER)],)
    def delete(self, request):
        try:
            id = request.query_params["id"]
            if id != None:
                weather = Weather.objects.get(id=id)
            weather.delete()
            return response.Response(status=st.HTTP_204_NO_CONTENT)
        except Weather.DoesNotExist:
            return response.Response(status=st.HTTP_404_NOT_FOUND)


class GetByDateWeatherAPIView(APIView):
    @swagger_auto_schema(
        responses={200: openapi.Response('ok', GetWeatherSerializer)},
        manual_parameters=[openapi.Parameter('date', openapi.IN_QUERY, description="Get weather by date", type=openapi.TYPE_STRING)],)
    def get(self, request):
        date = request.query_params['date']
        if date != None:
            weather = Weather.objects.filter(date=date)
            return response.Response(data=GetWeatherSerializer(weather, many=True).data, status=st.HTTP_200_OK)
        return response.Response(status=st.HTTP_400_BAD_REQUEST)


class RegisterUserAPIView(APIView):
    permission_classes = (permissions.IsAdminUser,)

    @swagger_auto_schema(
        responses={201: openapi.Response('created', UserSerializer)},
        request_body=UserSerializer)
    def post(self, request):
        data = request.data
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name']
        )
        user.set_password(data['password'])
        user.save()
        return response.Response(data=UserSerializer(user).data, status=st.HTTP_201_CREATED)


class EditUserAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    @swagger_auto_schema(
        responses={202: openapi.Response('update success', UserSerializer)},
        request_body=EditUserSerializer)
    def post(self, request):
        data = request.data
        try:
            if not EditUserSerializer(data=data).is_valid():
                return response.Response(status=st.HTTP_400_BAD_REQUEST)
            user = request.user
            user.email = data['email']
            user.set_password(data['password'])
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.save()
            return response.Response(data=UserSerializer(user).data, status=st.HTTP_202_ACCEPTED)
        except User.DoesNotExist:
            return response.Response(status=st.HTTP_404_NOT_FOUND)
        except:
            return response.Response(status=st.HTTP_400_BAD_REQUEST)
