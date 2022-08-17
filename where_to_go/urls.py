from django.contrib import admin
from places import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from settings import DEBUG


urlpatterns = [
    path('tinymce/', include('tinymce.urls'), ),
    path('admin/', admin.site.urls),
    path('', views.show_home),
    path('places/<event_id>', views.show_event, name='event')
]

if DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)