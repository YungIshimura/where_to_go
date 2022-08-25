import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Event, Image


class Command(BaseCommand):
    help = 'Send a link to a page that contains the desired data in json format'

    def handle(self, url, **options):
        response = requests.get(url)
        response.raise_for_status()
        place = response.json()
        event, created = Event.objects.get_or_create(
            title=place['title'],
            defaults={
                'short_description': place.setdefault('description_short', ''),
                'long_description': place.setdefault('description_long', ''),
                'longitude': place['coordinates']['lng'],
                'latitude': place['coordinates']['lat']
            })

        if created:
            for image in place['imgs']:
                response = requests.get(image)
                response.raise_for_status()
                Image.objects.create(event=event, image=ContentFile(
                    response.content, name=f'{event.id} {event.title}'))

    def add_arguments(self, parser):
        parser.add_argument(
            nargs='?',
            type=str,
            dest='url'
        )
