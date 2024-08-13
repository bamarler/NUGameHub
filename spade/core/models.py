from django.db import models
from django.utils.text import slugify

class Game(models.Model):
    STATUS_CHOICES = [
        ('developing', 'Developing'),
        ('in_review', 'In Review'),
        ('published', 'Published'),
    ]

    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    js_file = models.FileField(upload_to='games/js/', null=True, blank=True)  # For the .js file
    cover_image = models.ImageField(upload_to='games/images/', null=True, blank=True)  # For a cover image
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='developing')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
