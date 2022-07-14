from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(verbose_name='Название мероприятия',max_length=250)
    description_short = models.TextField(verbose_name='Краткое описание мероприятия')
    description_long = models.TextField(verbose_name='Полное описание мероприятия')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    event = models.ForeignKey('Event', on_delete=models.SET_NULL,
                              verbose_name='Мероприятие',
                              related_name='images',
                              null=True)
    image = models.ImageField(verbose_name='Изображения')
    
    def __str__(self):
        return f'{self.id} {self.event.title}'