from django.db import models
from apps.common.models import BaseModel
from django_ckeditor_5.fields import CKEditor5Field
from pytils.translit import slugify



class Service(BaseModel):
    """Услуги"""
    # Основная информация
    title = models.CharField(max_length=255, verbose_name='Название услуги')
    slug = models.CharField("Название услуги", max_length=255,
                            editable=False, blank=True, null=True, db_index=True)
    ment_title = models.TextField(blank=True, verbose_name='Meta Title')
    meta_description = models.TextField(blank=True, verbose_name='Meta Description')
    short_description = models.TextField(blank=True, verbose_name='Короткое описание (для карточки)')
    
    # Медиа для карточки
    icon = models.FileField(upload_to='services/icons/', blank=True, null=True, verbose_name='Иконка (SVG)')
    
    # Медиа для страницы услуги
    video_background = models.FileField(upload_to='services/videos/', blank=True, null=True, verbose_name='Видео на задний фон')
    image_background = models.ImageField(upload_to='services/backgrounds/', blank=True, null=True, verbose_name='Фото на задний фон')
    description_image = models.ImageField(upload_to='services/descriptions/', blank=True, null=True, verbose_name='Фото на описание')

    show_video = models.BooleanField('показывать видеоплеер',default=False,null=False, blank=True)
    vk_video = models.TextField('VK видео', blank=True, null=True)

    # Основное содержимое
    tags = models.TextField(blank=True, verbose_name='Тэги (через запятую)', null=True)
    description = CKEditor5Field(verbose_name='Описание услуги', blank=True, config_name='extends')
    
    # Связи
    industries = models.ManyToManyField(
        'data.Industry',
        related_name='services',
        blank=True,
        verbose_name='Отрасли применения'
    )
    projects = models.ManyToManyField(
        'data.Project',
        related_name='services',
        blank=True,
        verbose_name='Реализованные проекты'
    )
    reviews = models.ManyToManyField(
        'data.Review',
        related_name='services',
        blank=True,
        verbose_name='Отзывы клиентов'
    )
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def tags_list(self):
        """Возвращает список тэгов"""
        return [tag.strip() for tag in self.tags.split(',') if tag.strip()]


class ServiceAdvantage(BaseModel):
    """Преимущества услуги"""
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='advantages',
        verbose_name='Услуга'
    )
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок вывода')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Преимущество услуги'
        verbose_name_plural = 'Преимущества услуг'
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return f'{self.service.title} - {self.title}'


class ServiceTechnicalSpec(BaseModel):
    """Технические характеристики услуги"""
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='technical_specs',
        verbose_name='Услуга'
    )
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок вывода')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = CKEditor5Field(verbose_name='Контент', config_name='default')
    image = models.FileField(upload_to='services/specs/', blank=True, null=True, verbose_name='Прикрепленное фото (SVG)')
    
    class Meta:
        verbose_name = 'Техническая характеристика услуги'
        verbose_name_plural = 'Технические характеристики услуг'
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return f'{self.service.title} - {self.title}'


