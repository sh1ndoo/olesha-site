from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit, Transpose
from packaging.tags import Tag


class ScranItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, default='')
    place = models.CharField(max_length=255, default='')
    country = models.ForeignKey("Country", on_delete=models.SET_NULL, null=True)
    year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_moderated = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name='scrans')
    image = ProcessedImageField(
        verbose_name='Логотип', blank=False, null=False,
        processors=[
            Transpose(),
            ResizeToFit(width=800, upscale=False)
        ],
        format='WEBP',
        options={'quality': 80},
    )

    def __str__(self):
        return self.name

# class ScranCouple(models.Model):
#     scran1 = models.ForeignKey(
#         ScranItem,
#         on_delete=models.CASCADE,
#     )
#     scran2 = models.ForeignKey(
#         ScranItem,
#         on_delete=models.CASCADE,
#     )
#
# class Scrandle(models.Model):
#     scran_couples = models.ManyToManyField(ScranCouple)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name