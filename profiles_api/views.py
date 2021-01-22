from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        """Return list of api views featuresss"""

        an_apiview = [
            'hi faheem',
            'loki',
            'chawal'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
