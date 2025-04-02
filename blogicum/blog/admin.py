from django.contrib import admin

# Register your models here.
from .models import Category, Location, Post

admin.site.site_header = "Администрирование блога"
admin.site.site_title = "Панель управления"
admin.site.index_title = "Управление контентом"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published", "created_at")
    search_fields = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published", "created_at")
    search_fields = ("name", )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "location", "is_published", "pub_date")
    list_filter = ("category", "is_published", "pub_date")
    search_fields = ("title", "text")
    date_hierarchy = "pub_date"
