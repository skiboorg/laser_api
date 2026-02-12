from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.data.models import Project
from apps.data.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """ViewSet для реализованных проектов"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
