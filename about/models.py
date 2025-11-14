from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    # Image for the about page (optional)
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    @property
    def image_url(self):
        """
        Return a usable image URL for templates.
        - If an uploaded image is set and exists in storage, return its URL.
        - Otherwise return the static fallback path `images/nobody.jpg`.
        This avoids templates trying to load missing media files in production.
        """
        from django.templatetags.static import static
        try:
            if self.image and getattr(self.image, 'name', None):
                # storage.exists() is storage backend safe (works for default FileSystemStorage)
                if self.image.storage.exists(self.image.name):
                    return self.image.url
        except Exception:
            # any issue (missing storage, permissions) -> fall back to static
            pass
        return static('images/nobody.jpg')

    def __str__(self):
        return self.title