from django.db import models
from apps.common.models import BaseModel
from django_ckeditor_5.fields import CKEditor5Field
from pytils.translit import slugify



class Equipment(BaseModel):
    """Оборудование"""
    # Основная информация
    title = models.CharField(max_length=255, verbose_name='Название оборудования')
    slug = models.CharField("Название услуги", max_length=255,
                            editable=False, blank=True, null=True, db_index=True)
    meta_description = models.TextField(blank=True, verbose_name='Meta Description')
    short_description = models.TextField(blank=True, verbose_name='Короткое описание (для главной)')
    
    # Медиа
    main_image = models.ImageField(upload_to='equipment/main/', blank=True, null=True, verbose_name='Основное фото (на главной)')
    background_image = models.ImageField(upload_to='equipment/backgrounds/', blank=True, null=True, verbose_name='Фото на задний фон')
    
    # Основное содержимое
    description = CKEditor5Field(verbose_name='Описание оборудования', blank=True, config_name='default')
    
    # Связи
    industries = models.ManyToManyField(
        'data.Industry',
        related_name='equipment',
        blank=True,
        verbose_name='Отрасли применения'
    )
    reviews = models.ManyToManyField(
        'data.Review',
        related_name='equipment',
        blank=True,
        verbose_name='Отзывы клиентов'
    )
    
    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class EquipmentAdvantage(BaseModel):
    """Преимущества оборудования"""
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name='advantages',
        verbose_name='Оборудование'
    )
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок вывода')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Преимущество оборудования'
        verbose_name_plural = 'Преимущества оборудования'
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return f'{self.equipment.title} - {self.title}'


class EquipmentTechnicalSpec(BaseModel):
    """Технические характеристики оборудования"""
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name='technical_specs',
        verbose_name='Оборудование'
    )
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок вывода')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = CKEditor5Field(verbose_name='Контент', config_name='default')
    image = models.FileField(upload_to='equipment/specs/', blank=True, null=True, verbose_name='Прикрепленное фото (SVG)')
    
    class Meta:
        verbose_name = 'Техническая характеристика оборудования'
        verbose_name_plural = 'Технические характеристики оборудования'
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return f'{self.equipment.title} - {self.title}'


class EquipmentPhoto(BaseModel):
    """Фотографии оборудования"""
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='Оборудование'
    )
    image = models.ImageField(upload_to='equipment/photos/', verbose_name='Фотография')
    title = models.CharField(max_length=255, blank=True, verbose_name='Заголовок фото')
    description = models.TextField(blank=True, verbose_name='Описание фото')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок вывода')
    
    class Meta:
        verbose_name = 'Фотография оборудования'
        verbose_name_plural = 'Фотографии оборудования'
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return f'{self.equipment.title} - {self.title or "Фото"}'
