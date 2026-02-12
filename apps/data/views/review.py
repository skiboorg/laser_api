from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.data.models import Review
from apps.data.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet для отзывов клиентов"""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'uuid'
