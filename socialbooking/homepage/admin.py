from django.contrib import admin
from django.utils.html import format_html


from .models import Featured


@admin.register(Featured)
class FeaturedAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'stay', 'preview',)
    readonly_fields = ('preview',)

    def preview(self, obj):
        return format_html('<img src="{}" height="100" />'.format(obj.photo.image.url))
