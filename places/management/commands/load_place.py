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
        event = Event.objects.get_or_create(title=event_json['title'],
                                    defaults={
                                    'short_description': event_json.setdefault('description_short', ''),
                                    'long_description': event_json.setdefault('description_long', ''),
                                    'longitude':event_json['coordinates']['lng'],
                                    'latitude': event_json['coordinates']['lat']
                                    })
        if event[1]:
            for image in event_json['imgs']:
                response = requests.get(image)
                response.raise_for_status()
                Image.objects.create(event=event[0], image=ContentFile(response.content, name=f'{event[0].id} {event[0].title}' ))

    def add_arguments(self, parser):
        parser.add_argument(
            nargs='?',
            type=str,
            dest='url'
        )
