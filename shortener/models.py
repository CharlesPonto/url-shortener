from django.db import models

# Create your models here.

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
