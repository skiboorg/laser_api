from django.db import models
from apps.common.models import BaseModel
from django_ckeditor_5.fields import CKEditor5Field


class Review(BaseModel):
    """Отзывы клиентов"""
    tags = models.CharField(max_length=500, blank=True, verbose_name='Тэги (через запятую)')
    photo = models.ImageField(upload_to='reviews/', blank=True, null=True, verbose_name='Фото человека')
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=255, blank=True, verbose_name='Подпись к ФИО')
    text = CKEditor5Field(verbose_name='Текст отзыва', config_name='default')
    
    class Meta:
        verbose_name = 'Отзыв клиента'
        verbose_name_plural = 'Отзывы клиентов'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.full_name} - {self.position}'
    
    @property
    def tags_list(self):
        """Возвращает список тэгов"""
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
