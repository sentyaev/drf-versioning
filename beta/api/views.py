from rest_framework import viewsets

from .v1.serializers import BetaSerializer as BetaSerializer_v1
from .v2.serializers import BetaSerializer as BetaSerializer_v2

from ..models import Beta
from ..mixins import SerializerClassMixin


version_map = {
    'v1': BetaSerializer_v1,
    'v2': BetaSerializer_v2,
}


class BetaViewSet(SerializerClassMixin, viewsets.ModelViewSet):
    version_map = version_map
    queryset = Beta.objects.all()
