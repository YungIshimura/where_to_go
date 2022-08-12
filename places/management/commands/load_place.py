from django.core.management.base import BaseCommand
import requests
from places.models import Event, Image
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Trash'

    def handle(self, url, **options):
        response = requests.get(url)
        response.raise_for_status()
        event_json = response.json()
        Event.objects.get_or_create(title=event_json['title'],
                                    short_description=event_json['description_short'],
                                    long_description=event_json['description_long'],
                                    longitude=event_json['coordinates']['lng'],
                                    latitude=event_json['coordinates']['lat'])
        event = Event.objects.get(title=event_json['title'])

        for image in event_json['imgs']:
            response = requests.get(image)
            response.raise_for_status
            binary_image = response.content
            image = Image.objects.create(event=event)
            image.image.save(f'{event.id} {event.title}',
                             ContentFile(binary_image),
                             save=True)

    def add_arguments(self, parser):
        parser.add_argument(
            nargs='?',
            type=str,
            dest='url'
        )
