from rest_framework import serializers

from ..models import Alpha


class AlphaSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        validated_data['version2'] = 1
        return super().create(validated_data)

    class Meta:
        model = Alpha
        fields = ('url', 'version1')
