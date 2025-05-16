from django.contrib import admin
from .models import ShortenedURL

@admin.register(ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'original_url', 'created_at', 'click_count')
    search_fields = ('short_code', 'original_url')
