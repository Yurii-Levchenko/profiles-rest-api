from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    def get(self, request, format=None):
        an_apiview = [
        'Uses HTTP methods as functions (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped mannually to URLs',
        ]
    
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
