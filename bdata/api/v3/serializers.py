from rest_framework import serializers

from bdata.models import BData


class BDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BData
        fields = ('url', 'version1', 'version2', 'version3')
