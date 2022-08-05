from django.shortcuts import render
from .models import Event


def home(request):
    events = Event.objects.all()
    features = {}
    event_features = []
    for event in events:
      event_features.append({
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
    features['features'] = event_features
    return render(request, 'index.html', context=features)
    