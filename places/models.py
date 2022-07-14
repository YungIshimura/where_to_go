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