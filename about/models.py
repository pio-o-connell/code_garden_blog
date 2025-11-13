from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    # Image for the about page (optional)
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title