from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        default='',
        editable=False,
    )

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class Message(models.Model):
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content} [{self.date_added}]'

    class Meta:
        ordering = ('-date_added',)


