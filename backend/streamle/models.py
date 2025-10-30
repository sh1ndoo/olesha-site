import uuid

from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, Transpose
from packaging.tags import Tag


class StreamItem(models.Model):
    id_stream = models.PositiveBigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    avg_viewers = models.IntegerField(default=0)
    max_viewers = models.IntegerField(default=0)
    date = models.DateTimeField()
    date_added = models.DateTimeField(auto_now_add=True)
    length = models.IntegerField(default=0)
    view_minutes = models.IntegerField(default=0)
    games_played = models.ManyToManyField("Game", related_name="streams")
    follower_gain = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField()

    def __str__(self):
        return self.title


# class StreamleItem(models.Model):
#     stream = models.ManyToManyField(StreamItem)

