from django.contrib import admin
from apps.data.models import Service, ServiceAdvantage, ServiceTechnicalSpec


class ServiceAdvantageInline(admin.TabularInline):
    model = ServiceAdvantage
    extra = 0
    fields = ['order', 'title', 'description']
    ordering = ['order']


class ServiceTechnicalSpecInline(admin.StackedInline):
    model = ServiceTechnicalSpec
    extra = 0
    fields = ['order', 'title', 'content', 'image']
    ordering = ['order']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'short_description', 'description', 'tags']
    list_filter = ['created_at', 'industries']
    readonly_fields = ['uuid', 'created_at', 'updated_at']
    filter_horizontal = ['industries', 'projects', 'reviews']
    inlines = [ServiceAdvantageInline, ServiceTechnicalSpecInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'meta_description','ment_title', 'short_description', 'tags')
        }),
        ('Медиа для карточки', {
            'fields': ('icon',)
        }),
        ('Медиа для страницы', {
            'fields': ('video_background', 'image_background', 'description_image','show_video','vk_video',),
            'classes': ('collapse',)
        }),
        ('Описание', {
            'fields': ('description',)
        }),
        ('Связи', {
            'fields': ('industries', 'projects', 'reviews'),
            'classes': ('collapse',)
        }),
        ('Системная информация', {
            'fields': ('uuid', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
