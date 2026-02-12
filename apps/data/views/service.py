from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.data.models import Service
from apps.data.serializers import ServiceListSerializer, ServiceDetailSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """ViewSet для услуг"""
    queryset = Service.objects.prefetch_related(
        'advantages',
        'technical_specs',
        'industries',
        'projects',
        'reviews'
    ).all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        """Используем разные сериализаторы для списка и детальной информации"""
        if self.action == 'list':
            return ServiceListSerializer
        return ServiceDetailSerializer
