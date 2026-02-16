from django.contrib import admin
from apps.data.models.news import NewsItem, Image
from apps.data.models.cb import CallbackForm

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'order_num', 'show_on_main']
    inlines = [ImageInline]

@admin.register(CallbackForm)
class CallbackFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'created_at','is_done']
