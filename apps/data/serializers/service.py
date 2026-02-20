from rest_framework import serializers
from apps.data.models import Service, ServiceAdvantage, ServiceTechnicalSpec
from .industry import IndustrySerializer
from .project import ProjectSerializer
from .review import ReviewSerializer
from apps.data.models.cb import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class ServiceAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAdvantage
        fields = ['uuid', 'order', 'title', 'description', 'created_at', 'updated_at']
        read_only_fields = ['uuid', 'created_at', 'updated_at']


class ServiceTechnicalSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTechnicalSpec
        fields = ['uuid', 'order', 'title', 'content', 'image', 'created_at', 'updated_at']
        read_only_fields = ['uuid', 'created_at', 'updated_at']


class ServiceListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка услуг (карточки)"""
    tags_list = serializers.ReadOnlyField()
    
    class Meta:
        model = Service
        fields = [
            'uuid',
            'title',
            'short_description',
            'icon',
            'slug',
            'tags',
            'tags_list',
            'created_at',
        ]
        read_only_fields = ['uuid', 'created_at']


class ServiceDetailSerializer(serializers.ModelSerializer):
    """Детальный сериализатор услуги со всеми связями"""
    tags_list = serializers.ReadOnlyField()
    advantages = ServiceAdvantageSerializer(many=True, read_only=True)
    technical_specs = ServiceTechnicalSpecSerializer(many=True, read_only=True)
    industries = IndustrySerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Service
        fields = [
            'uuid',
            'title',
            'ment_title',
            'meta_description',
            'short_description',
            'icon',
            'video_background',
            'image_background',
            'description_image',
            'tags',
            'tags_list',
            'description',
            'advantages',
            'technical_specs',
            'industries',
            'projects',
            'reviews',
            'show_video',
            'vk_video',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['uuid', 'created_at', 'updated_at']
