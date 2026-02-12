from .industry import IndustrySerializer
from .service import (
    ServiceListSerializer,
    ServiceDetailSerializer,
    ServiceAdvantageSerializer,
    ServiceTechnicalSpecSerializer,
)
from .equipment import (
    EquipmentListSerializer,
    EquipmentDetailSerializer,
    EquipmentAdvantageSerializer,
    EquipmentTechnicalSpecSerializer,
    EquipmentPhotoSerializer,
)
from .review import ReviewSerializer
from .project import ProjectSerializer

__all__ = [
    'IndustrySerializer',
    'ServiceListSerializer',
    'ServiceDetailSerializer',
    'ServiceAdvantageSerializer',
    'ServiceTechnicalSpecSerializer',
    'EquipmentListSerializer',
    'EquipmentDetailSerializer',
    'EquipmentAdvantageSerializer',
    'EquipmentTechnicalSpecSerializer',
    'EquipmentPhotoSerializer',
    'ReviewSerializer',
    'ProjectSerializer',
]
