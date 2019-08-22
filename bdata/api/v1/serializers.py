from rest_framework import serializers

from bdata.models import BData


class BDataSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        validated_data['age'] = 0
        return super().create(validated_data)

    class Meta:
        model = BData
        fields = ('url', 'version1')
