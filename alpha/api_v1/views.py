from rest_framework import viewsets

from .serializers import AlphaSerializer
from ..models import Alpha


class AlphaViewSet(viewsets.ModelViewSet):
    queryset = Alpha.objects.all()
    serializer_class = AlphaSerializer
