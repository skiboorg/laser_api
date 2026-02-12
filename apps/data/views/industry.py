from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.data.models import Industry
from apps.data.serializers import IndustrySerializer


class IndustryViewSet(viewsets.ModelViewSet):
    """ViewSet для отраслей применения"""
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'uuid'
