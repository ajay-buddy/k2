from rest_framework import serializers

from kinstance.models import KInstance

class KInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = KInstance
        fields = [
            'kinstance_id',
            'name',
            'description',
            'created_by',
            'updated_by',
            'created_at',
            'updated_at'
        ]

    # def validate(self, value):
    #     return