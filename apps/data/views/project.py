from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.data.models import Project
from apps.data.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet для реализованных проектов"""
    #queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

    def get_queryset(self):
        at_index = self.request.query_params.get('index', False)
        if at_index == 'true':
            return Project.objects.filter(show_at_index=True)
        return Project.objects.all()
