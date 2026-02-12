from django.db import models
from apps.common.models import BaseModel


class Industry(BaseModel):
    """Отрасли применения"""
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Отрасль применения'
        verbose_name_plural = 'Отрасли применения'
        ordering = ['name']
    
    def __str__(self):
        return self.name
