import uuid
from django.db import models

class TimeStampedModel(models.Model):
    """Абстрактная модель с метками времени"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    
    class Meta:
        abstract = True

class UUIDModel(models.Model):
    """Абстрактная модель с UUID"""
    uuid = models.UUIDField(
        default=uuid.uuid4, 
        editable=False, 
        unique=True,
        verbose_name='UUID'
    )
    
    class Meta:
        abstract = True

class BaseModel(TimeStampedModel, UUIDModel):
    """Базовая модель с UUID и метками времени"""
    class Meta:
        abstract = True
