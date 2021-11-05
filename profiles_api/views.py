from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self,request,format = None):
        an_api = [
            'Usees Http methods as functon (get,post,put,patch,delete)',
            'Is similat to a traditional Django View',
            'Gives you the most control over your logic'
        ]
        
        return Response({'an_apiview':an_api, 'message': 'Hello World'})