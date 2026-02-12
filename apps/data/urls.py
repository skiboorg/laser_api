from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.data.views import (
    IndustryViewSet,
    ServiceViewSet,
    EquipmentViewSet,
    ReviewViewSet,
    ProjectViewSet,
)

router = DefaultRouter()
router.register(r'industries', IndustryViewSet, basename='industry')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'equipment', EquipmentViewSet, basename='equipment')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('', include(router.urls)),
]
