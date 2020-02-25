from rest_framework import serializers

from ktags.models import KTags

class KTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = KTags
        fields = [
            'ktag_id',
            'name',
            'description',
            'created_by',
            'updated_by',
            'created_at',
            'updated_at'
        ]

    # def validate(self, value):
    #     return