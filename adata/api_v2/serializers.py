from rest_framework import serializers

from ..models import AData


class ADataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AData
        fields = ('url', 'version1', 'version2')
