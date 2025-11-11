from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title','content']
    list_filter = ('status','created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
# 	list_display = ("title", "author", "created_on", "status")
# 	prepopulated_fields = {"slug": ("title",)}
# 	search_fields = ("title", "content")
# 	list_filter = ("status", "created_on")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ("post", "author", "created_on", "approved")
	search_fields = ("body",)
	list_filter = ("approved", "created_on")
