from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth import get_user_model


class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    date_picker = models.DateField(null=True, blank=True)
    time_picker = models.TimeField(blank=False)
    end_picker = models.TimeField(blank=False, default=None, null=True)
    thumbnail = models.ImageField(upload_to='event_images', default=None, null=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        null=True, default=None
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("event_detail", args=[self.id])
    