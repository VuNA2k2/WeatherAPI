from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, response, status
from rest_framework.views import APIView
from .serializers import GetLocationSerializer, PostLocationSerializer

from .models import Location

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
            location.city = data.data['city']
            location.country = data.data['country']
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


