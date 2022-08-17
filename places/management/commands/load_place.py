from django.core.management.base import BaseCommand
import requests
from places.models import Event, Image
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Send a link to a page that contains the desired data in json format'

    def handle(self, url, **options):
        response = requests.get(url)
        response.raise_for_status()
        event_json = response.json()
        Event.objects.get_or_create(title=event_json['title'],
                                    defaults={
                                    'short_description': event_json.setdefault('description_short', ''),
                                    'long_description': event_json.setdefault('description_long', ''),
                                    'longitude':event_json['coordinates']['lng'],
                                    'latitude': event_json['coordinates']['lat']
                                    })
        event = Event.objects.get(title=event_json['title'])

        for image in event_json['imgs']:
            response = requests.get(image)
            response.raise_for_status()
            image = Image.objects.create(event=event, image=ContentFile(response.content, name=f'{event.id} {event.title}' ))

    def add_arguments(self, parser):
        parser.add_argument(
            nargs='?',
            type=str,
            dest='url'
        )
