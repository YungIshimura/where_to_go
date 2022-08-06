from django.db import models
from tinymce.models import HTMLField

class Event(models.Model):
    title = models.CharField(verbose_name='Название мероприятия',max_length=250)
    short_description = models.TextField(verbose_name='Краткое описание мероприятия')
    long_description = HTMLField(verbose_name='Полное описание мероприятия')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')
    order = models.IntegerField(
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ("-order",)

    def __str__(self):
        return self.title


class Image(models.Model):
    event = models.ForeignKey('Event', on_delete=models.SET_NULL,
                              verbose_name='Мероприятие',
                              related_name='images',
                              null=True)
    image = models.ImageField(verbose_name='Изображения')
    order = models.IntegerField(
        default=0,
        blank=False,
        null=False
    )

    class Meta:
        ordering = ("-order",)

    def __str__(self):
        return f'{self.id}'