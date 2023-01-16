from rest_framework import serializers
from core.models import Trash, Bucket

class BucketSerializer(serializers.Serializer):
    class Meta:
        model = Bucket
        fields = "__all__"

class TrashSerializer(serializers.Serializer):
    class Meta:
        model = Trash
        fields = "__all__"