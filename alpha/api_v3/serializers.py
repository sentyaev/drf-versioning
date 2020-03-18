from rest_framework import serializers

from ..models import Alpha


class AlphaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alpha
        fields = ('url', 'version1', 'version2', 'version3')
