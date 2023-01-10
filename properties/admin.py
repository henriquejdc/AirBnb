from django.contrib import admin

from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'activated_date',
        'cleaning_value',
        'accepts_animals',
        'max_number_guests',
        'bathrooms'
    )


admin.site.register(Property, PropertyAdmin)
