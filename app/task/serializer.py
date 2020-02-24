from rest_framework import serializers

from task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'task_id',
            # 'space_id',
            'project_id',
            # 'board_id',
            'name',
            'description',
            'created_by',
            'updated_by',
            'created_at',
            'updated_at'
        ]

    # def validate(self, value):
    #     return