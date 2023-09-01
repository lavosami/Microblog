from django.db import models
from django.urls import reverse

"""
title = the title of the post
content = the text of the post
photo = the picture in the post
time_created = date and time when post was created
time_update = date and time of post's last update
is_published = post was published/in waiting list
"""


class Music(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
