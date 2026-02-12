from rest_framework import serializers
from apps.data.models import Equipment, EquipmentAdvantage, EquipmentTechnicalSpec, EquipmentPhoto
from .industry import IndustrySerializer
from .review import ReviewSerializer


class EquipmentAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentAdvantage
        fields = ['uuid', 'order', 'title', 'description', 'created_at', 'updated_at']
        read_only_fields = ['uuid', 'created_at', 'updated_at']


class EquipmentTechnicalSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentTechnicalSpec
        fields = ['uuid', 'order', 'title', 'content', 'image', 'created_at', 'updated_at']
        read_only_fields = ['uuid', 'created_at', 'updated_at']


class EquipmentPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentPhoto
        fields = ['uuid', 'image', 'title', 'description', 'order', 'created_at', 'updated_at']
        read_only_fields = ['uuid', 'created_at', 'updated_at']


class EquipmentListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка оборудования (карточки на главной)"""
    
    class Meta:
        model = Equipment
        fields = [
            'uuid',
            'title',
            'slug',
            'short_description',
            'main_image',
            'created_at',
        ]
        read_only_fields = ['uuid', 'created_at']


class EquipmentDetailSerializer(serializers.ModelSerializer):
    """Детальный сериализатор оборудования со всеми связями"""
    advantages = EquipmentAdvantageSerializer(many=True, read_only=True)
    technical_specs = EquipmentTechnicalSpecSerializer(many=True, read_only=True)
    photos = EquipmentPhotoSerializer(many=True, read_only=True)
    industries = IndustrySerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Equipment
        fields = [
            'uuid',
            'title',
            'meta_description',
            'short_description',
            'main_image',
            'background_image',
            'description',
            'advantages',
            'technical_specs',
            'photos',
            'industries',
            'reviews',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['uuid', 'created_at', 'updated_at']
