from rest_framework.viewsets import generics
from .serializers import TrashSerializer
from core.models import Trash

class GetAllTrashes(generics.ListAPIView):
    serializer_class = TrashSerializer
    queryset = Trash.objects.all()

class GetTrash(generics.RetrieveAPIView):
    serializer_class = TrashSerializer
    queryset = Trash

