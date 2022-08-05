from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Event


def home(request):
    events = Event.objects.all()
    features = {}
    event_details = []
    for event in events:
      event_details.append({
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [event.longitude, event.latitude]
          },
          "properties": {
            "title": event.title,
            "placeId": event.id,
            "detailsUrl": "static/places/moscow_legends.json"
          }
        },
      )
    features['features'] = event_details
    return render(request, 'index.html', context=features)


def event(request, event_id):
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
  return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False, 'indent':2})