from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Event


def show_home(request):
    events = Event.objects.all()
    event_details = [{
        "type": "Feature",
        "geometry": {
          "type": "Point",
          "coordinates": [event.longitude, event.latitude]
           },

          "properties": {
          "title": event.title,
          "placeId": event.id,
          "detailsUrl": reverse('event', args=(event.id, ))
         }

       } for event in events]

    features = {'features': event_details}

    return render(request, 'index.html', context=features)


def show_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    response = {
      "title": event.title,
      "imgs": [image.image.url for image in event.images.all()],
      "description_short": event.short_description,
      "description_long": event.long_description,
      "coordinates": {
        "lat": event.latitude,
        "lng": event.longitude
        }
      }

    return JsonResponse(response,
                        json_dumps_params={'ensure_ascii': False, })
