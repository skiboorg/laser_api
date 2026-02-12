from rest_framework import serializers
from apps.data.models import Industry


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ['uuid', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['uuid', 'created_at', 'updated_at']
