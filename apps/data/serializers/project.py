from rest_framework import serializers
from apps.data.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    tags_list = serializers.ReadOnlyField()
    class Meta:
        model = Project
        fields = ['uuid', 'title','slug','tags_list', 'description', 'image', 'created_at', 'updated_at']
        read_only_fields = ['uuid', 'created_at', 'updated_at']
