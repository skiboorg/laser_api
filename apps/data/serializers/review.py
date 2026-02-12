from rest_framework import serializers
from apps.data.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    tags_list = serializers.ReadOnlyField()
    
    class Meta:
        model = Review
        fields = [
            'uuid',
            'tags',
            'tags_list',
            'photo',
            'full_name',
            'position',
            'text',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['uuid', 'created_at', 'updated_at']
