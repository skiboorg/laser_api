from django.contrib import admin
from apps.data.models.news import NewsItem, Image

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'order_num', 'show_on_main']
    inlines = [ImageInline]