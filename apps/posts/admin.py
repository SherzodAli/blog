from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Админ-панель для постов."""

    fields = ['title', 'summary', 'image']
    list_display = ['id', 'title', 'slug', 'summary', 'admin_photo', 'date']
    list_display_links = ['title']
    search_fields = ['title', 'summary']
    ordering = ['-id']
