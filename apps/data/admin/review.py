from django.contrib import admin
from apps.data.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'created_at']
    search_fields = ['full_name', 'position', 'text', 'tags']
    list_filter = ['created_at']
    readonly_fields = ['uuid', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Информация о клиенте', {
            'fields': ('full_name', 'position', 'photo')
        }),
        ('Отзыв', {
            'fields': ('tags', 'text')
        }),
        ('Системная информация', {
            'fields': ('uuid', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
