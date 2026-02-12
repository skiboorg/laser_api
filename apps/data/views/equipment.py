from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.data.models import Equipment
from apps.data.serializers import EquipmentListSerializer, EquipmentDetailSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    """ViewSet для оборудования"""
    queryset = Equipment.objects.prefetch_related(
        'advantages',
        'technical_specs',
        'photos',
        'industries',
        'reviews'
    ).all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        """Используем разные сериализаторы для списка и детальной информации"""
        if self.action == 'list':
            return EquipmentListSerializer
        return EquipmentDetailSerializer
