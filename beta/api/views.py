from rest_framework import viewsets

from common.mixins import SerializerClassMixin

from .v1.serializers import BetaSerializer as BetaSerializer_v1
from .v2.serializers import BetaSerializer as BetaSerializer_v2
from .v3.serializers import BetaSerializer as BetaSerializer_v3

from ..models import Beta


version_map = {
    'v1': BetaSerializer_v1,
    'v2': BetaSerializer_v2,
    'v3': BetaSerializer_v3,
}


class BetaViewSet(SerializerClassMixin, viewsets.ModelViewSet):
    version_map = version_map
    queryset = Beta.objects.all()