from django.contrib import admin
from django.utils.html import format_html
from .models import Event, Image


class ImageInline(admin.TabularInline):
    readonly_fields = ['event_image', ]
    def event_image(self, obj):
        return format_html('<img src="{url}" width="350px" height="200px" />'.format(
            url = obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
            )
        )
    
    model = Image
    fields = ['image', 'event_image', ] 


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

admin.site.register(Image)