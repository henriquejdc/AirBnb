from django.contrib import admin

from .models import Advert


class AdvertAdmin(admin.ModelAdmin):
    list_display = (
        'platform',
        'platform_tax',
        'property',
    )


admin.site.register(Advert, AdvertAdmin)
