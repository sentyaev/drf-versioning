from rest_framework import viewsets

from .serializers import ADataSerializer
from ..models import AData


class ADataViewSet(viewsets.ModelViewSet):
    queryset = AData.objects.all()
    serializer_class = ADataSerializer
