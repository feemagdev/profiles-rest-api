from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test api view"""

    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Return list of api views featuresss"""

        an_apiview = [
            'hi faheem',
            'loki',
            'chawal'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """handle updating object"""
        return Response({'method': 'put method called'})

    def patch(self, request, pk=None):
        """handle partial updates of object"""
        return Response({'nethod': 'pathc mathod called'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method': 'delete method called'})
