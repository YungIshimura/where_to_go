from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from tinymce.models import HTMLField


class Event(models.Model):
    title = models.CharField(verbose_name='Название мероприятия',
                             max_length=250,
                             unique=True)

    short_description = models.TextField(
        verbose_name='Краткое описание мероприятия', blank=True)

    long_description = HTMLField(verbose_name='Полное описание мероприятия',
                                 blank=True)

    longitude = models.DecimalField(verbose_name='Долгота',
                                    max_digits=10,
                                    decimal_places=7,
                                    validators=[
                                        MinValueValidator(-180),
                                        MaxValueValidator(180)
                                    ])

    latitude = models.DecimalField(verbose_name='Широта',
                                   max_digits=9,
                                   decimal_places=7,
                                   validators=[
                                       MinValueValidator(-90),
                                       MaxValueValidator(90)
                                   ])

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
    )

    class Meta:
        ordering = ("-order",)

    def __str__(self):
        return f'{self.id} {self.event}'
