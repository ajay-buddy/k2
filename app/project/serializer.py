from rest_framework import serializers

from project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'project_id',
            # 'space_id',
            'name',
            'description',
            'created_by',
            'updated_by',
            'created_at',
            'updated_at'
        ]

    # def validate(self, value):
    #     return