from rest_framework import viewsets

from common.mixins import SerializerClassMixin

from .v1.serializers import BDataSerializer as BDataSerializer_v1
from .v2.serializers import BDataSerializer as BDataSerializer_v2
from .v3.serializers import BDataSerializer as BDataSerializer_v3

from ..models import BData


version_map = {
    'v1': BDataSerializer_v1,
    'v2': BDataSerializer_v2,
    'v3': BDataSerializer_v3,
}


class BDataViewSet(SerializerClassMixin, viewsets.ModelViewSet):
    version_map = version_map
    queryset = BData.objects.all()
