from rest_framework import serializers

from beta.models import Beta


class BetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beta
        fields = ('url', 'version1', 'version2', 'version3')
