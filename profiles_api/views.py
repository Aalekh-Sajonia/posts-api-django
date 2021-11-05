from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializers

    def get(self,request,format = None):
        an_api = [
            'Usees Http methods as functon (get,post,put,patch,delete)',
            'Is similat to a traditional Django View',
            'Gives you the most control over your logic'
        ]
        
        return Response({'an_apiview':an_api, 'message': 'Hello World'})
    
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST  
            )

    def put(self, request, pk = None):
        return Response({
            'method': 'PUT'
        })

    def patch(self, request, pk = None):
        return Response({
            'method': 'PATCH'
        })

    def delete(self, request, pk = None):
        return Response({
            'method': 'DELETE'
        })

class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializers

    def list(self,request):
        a_viewset = [
            'Usees Http methods as functon (get,post,put,patch,delete)',
            'Is similat to a traditional Django View',
            'Gives you the most control over your logic'
        ]

        return Response({
            'message': 'Hello',
            'a_viewset': a_viewset
        })
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data) 

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({
                'message': message
            })
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST  
            )

    def retrieve(self, request, pk = None):
        return Response({
            'http': 'GET'
        })

    def update(self,request, pk = None):

        return Response({
            'http': "PUT"
        })

    def partial_update(self, request, pk = None):
        return Response({
            'http': "PATCH"
        })

    def  destroy(self, request, pk = None):
        return Response({
            'http': "Delete"
        })

class UserProfileViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        serializer.save(user_profile = self.request.user)