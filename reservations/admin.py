from django.contrib import admin

from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'checkin_date',
        'checkout_date',
        'price',
        'comment',
        'number_guests',
        'advert'
    )
    readonly_fields = ('code',)


admin.site.register(Reservation, ReservationAdmin)
