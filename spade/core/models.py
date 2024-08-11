from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    js_file = models.FileField(upload_to='games/js/', null=True, blank=True)  # For the .js file
    cover_image = models.ImageField(upload_to='games/images/', null=True, blank=True)  # For a cover image

    def __str__(self):
        return self.name
