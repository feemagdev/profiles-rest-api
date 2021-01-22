from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """Serializes a name field to test our api view """

    name = serializers.CharField(max_length=10)
