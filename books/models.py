from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def upload_to(instance, filename):
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    return f'cover_images/{timestamp}_{filename}'


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, null=True, blank=True)
    cover_image = models.ImageField(upload_to=upload_to, null=True, blank=True)

    def __str__(self):
        return f'{self.title} by {self.author}'
