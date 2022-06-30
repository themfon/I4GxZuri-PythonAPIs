from rest_framework import serializers
from .models import Link

# create a serializer
class LinkSerializer(serializers.ModelSerializer):
    # initialize fields
    class Meta:
        model = Link
        fields = "__all__"