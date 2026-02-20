from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.data.views import (
    IndustryViewSet,
    ServiceViewSet,
    EquipmentViewSet,
    ReviewViewSet,
    ProjectViewSet,
)
from apps.data.views.news import GetNews,GetNewsItem, NewForm,TeamView

router = DefaultRouter()
router.register(r'industries', IndustryViewSet, basename='industry')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'equipment', EquipmentViewSet, basename='equipment')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('news/', GetNews.as_view()),
    path('news/<slug>/', GetNewsItem.as_view()),
    path('form', NewForm.as_view()),
    path('team/', TeamView.as_view()),
    path('', include(router.urls)),
]
