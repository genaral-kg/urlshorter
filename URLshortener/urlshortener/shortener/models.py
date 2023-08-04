from django.db import models

# Create your models here.
# shortener/models.py
from django.db import models
import string
import random
import datetime

class ShortURL(models.Model):
    long_url = models.URLField(unique=True)
    short_code = models.CharField(max_length=6, unique=True)
    clicks = models.PositiveIntegerField(default=0)
    expiration_date = models.DateTimeField(default=datetime.datetime.now() + datetime.timedelta(days=30))

    def save(self, *args, **kwargs):
        if not self.pk:
            self.short_code = self.generate_short_code()
        super().save(*args, **kwargs)

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))  # Используем 6 символов
