from django.contrib import admin
from .models import Post

@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "views_count", "created_at",)
    list_display_links = ("id", "title",)
    list_filter = ("is_published", "created_at",)
    search_fields = ("title", "content",)
    list_editable = ("is_published",)
