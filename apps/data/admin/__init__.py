from .industry import IndustryAdmin
from .service import ServiceAdmin, ServiceAdvantageInline, ServiceTechnicalSpecInline
from .equipment import EquipmentAdmin, EquipmentAdvantageInline, EquipmentTechnicalSpecInline, EquipmentPhotoInline
from .review import ReviewAdmin
from .project import ProjectAdmin
from .news import NewsItemAdmin

__all__ = [
    'IndustryAdmin',
    'ServiceAdmin',
    'ServiceAdvantageInline',
    'ServiceTechnicalSpecInline',
    'EquipmentAdmin',
    'EquipmentAdvantageInline',
    'EquipmentTechnicalSpecInline',
    'EquipmentPhotoInline',
    'ReviewAdmin',
    'ProjectAdmin',
    'NewsItemAdmin',
]
