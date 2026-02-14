from rest_framework import serializers
from apps.data.models.news import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class NewsItemShortSerializer(serializers.ModelSerializer):
    tags_list = serializers.ReadOnlyField()
    class Meta:
        model = NewsItem
        fields = [
            'cover',
            'name',
            'slug',
            'short_description',
            'created',
            'tags_list',
        ]



class NewsItemSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    others = serializers.SerializerMethodField()
    tags_list = serializers.ReadOnlyField()
    class Meta:
        model = NewsItem
        fields = '__all__'

    def get_others(self, obj):
        # Берём любые 2 проекта, кроме текущего
        qs = NewsItem.objects.exclude(id=obj.id).only('name', 'slug', 'created')[:2]
        return NewsItemShortSerializer(qs, many=True).data