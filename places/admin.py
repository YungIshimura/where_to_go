from django.contrib import admin
from .models import Event, Image



class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

admin.site.register(Image)