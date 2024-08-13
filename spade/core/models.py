from django.db import models
from django.utils.text import slugify

class Game(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    js_file = models.FileField(upload_to='games/js/', null=True, blank=True)  # For the .js file
    cover_image = models.ImageField(upload_to='games/images/', null=True, blank=True)  # For a cover image
    slug = models.SlugField(max_length=100, unique=True, blank=True)  # Slug field

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
