from rest_framework.viewsets import generics
from rest_framework.generics import GenericAPIView
from .serializers import TrashSerializer
from core.models import Trash
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser


class GetAllTrashes(generics.ListAPIView):
    serializer_class = TrashSerializer
    queryset = Trash.objects.all()

class GetTrash(generics.RetrieveAPIView):
    serializer_class = TrashSerializer
    queryset = Trash

class AddTrash(generics.CreateAPIView):
    serializer_class = TrashSerializer





