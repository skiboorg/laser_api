from django.db import models
from apps.common.models import BaseModel
from django_ckeditor_5.fields import CKEditor5Field
from pytils.translit import slugify

class Project(BaseModel):
    """Реализованные проекты"""
    title = models.CharField(max_length=255, verbose_name='Название проекта')
    slug = models.CharField("Название услуги", max_length=255, editable=False, blank=True, null=True, db_index=True)
    description = CKEditor5Field(verbose_name='Описание', blank=True, config_name='default')
    image = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name='Изображение')
    tags = models.TextField(blank=True, verbose_name='Тэги (через запятую)', null=True)

    class Meta:
        verbose_name = 'Реализованный проект'
        verbose_name_plural = 'Реализованные проекты'
        ordering = ['-created_at']
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def tags_list(self):
        """Возвращает список тэгов"""
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
    def __str__(self):
        return self.title
