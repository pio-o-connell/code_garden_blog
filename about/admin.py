from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

    readonly_fields = ('image_preview',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'image', 'image_preview')
        }),
    )

    def image_preview(self, obj):
        if obj and getattr(obj, 'image'):
            return f"<img src='{obj.image.url}' style='max-width:200px; height:auto;' />"
        return "(No image)"
    image_preview.allow_tags = True
    image_preview.short_description = 'Image preview'
