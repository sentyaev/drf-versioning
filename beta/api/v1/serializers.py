from rest_framework import serializers

from beta.models import Beta


class BetaSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        validated_data['mandatory_field_for_v2'] = 'default value'
        return super().create(validated_data)

    class Meta:
        model = Beta
        fields = ('url', 'version1')
