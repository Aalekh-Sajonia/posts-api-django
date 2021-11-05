from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

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