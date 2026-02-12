from django.contrib import admin
from apps.data.models import Equipment, EquipmentAdvantage, EquipmentTechnicalSpec, EquipmentPhoto


class EquipmentAdvantageInline(admin.TabularInline):
    model = EquipmentAdvantage
    extra = 0
    fields = ['order', 'title', 'description']
    ordering = ['order']


class EquipmentTechnicalSpecInline(admin.StackedInline):
    model = EquipmentTechnicalSpec
    extra = 0
    fields = ['order', 'title', 'content', 'image']
    ordering = ['order']


class EquipmentPhotoInline(admin.TabularInline):
    model = EquipmentPhoto
    extra = 0
    fields = ['order', 'image', 'title', 'description']
    ordering = ['order']


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'short_description', 'description']
    list_filter = ['created_at', 'industries']
    readonly_fields = ['uuid', 'created_at', 'updated_at']
    filter_horizontal = ['industries', 'reviews']
    inlines = [EquipmentAdvantageInline, EquipmentTechnicalSpecInline, EquipmentPhotoInline]
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'meta_description', 'short_description')
        }),
        ('Медиа', {
            'fields': ('main_image', 'background_image')
        }),
        ('Описание', {
            'fields': ('description',)
        }),
        ('Связи', {
            'fields': ('industries', 'reviews'),
            'classes': ('collapse',)
        }),
        ('Системная информация', {
            'fields': ('uuid', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
