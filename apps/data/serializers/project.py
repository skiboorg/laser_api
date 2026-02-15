from rest_framework import serializers
from apps.data.models import Project,ProjectImage

class ProjectImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectImage
        fields = '__all__'

class ProjectShortSerializer(serializers.ModelSerializer):
    tags_list = serializers.ReadOnlyField()
    class Meta:
        model = Project
        fields = ['uuid', 'title', 'slug', 'tags_list',  'image', 'created_at' ]

class ProjectSerializer(serializers.ModelSerializer):
    tags_list = serializers.ReadOnlyField()
    project_images = ProjectImageSerializer(many=True, read_only=True)
    others = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = ['uuid', 'title','slug','tags_list', 'description', 'image', 'created_at', 'updated_at','project_images','others']
        read_only_fields = ['uuid', 'created_at', 'updated_at']

    def get_others(self, obj):
        # Берём любые 2 проекта, кроме текущего
        qs = Project.objects.exclude(id=obj.id).only('title', 'slug', 'created_at')[:2]
        return ProjectShortSerializer(qs, many=True).data