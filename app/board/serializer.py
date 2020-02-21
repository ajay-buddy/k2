from rest_framework import serializers

from board.models import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = [
            'board_id',
            'project_id',
            'name',
            'description',
            'created_by',
            'updated_by',
            'created_at',
            'updated_at'
        ]

    # def validate(self, value):
    #     return