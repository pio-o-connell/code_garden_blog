from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "author", "created_on", "status")
	prepopulated_fields = {"slug": ("title",)}
	search_fields = ("title", "content")
	list_filter = ("status", "created_on")
