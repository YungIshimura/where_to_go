from django.contrib import admin
from django.utils.html import format_html
from .models import Event, Image
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    readonly_fields = ['event_image', ]
    def event_image(self, obj):
        return format_html('<img src="{url}" height="200px" />'.format(
            url = obj.image.url,
            )
        )
    
    model = Image
    fields = ['image', 'event_image', ] 


@admin.register(Event)
class EventAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline, 
    ]

admin.site.register(Image)