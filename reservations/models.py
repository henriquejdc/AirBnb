import random
import string

from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from adverts.models import Advert
from shared.models import BaseModelDate


# Create your models here.
class Reservation(BaseModelDate):
    code = models.CharField(
        unique=True,
        max_length=20,
        verbose_name=_("Reservation code")
    )
    checkin_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("Checkin date")
    )
    checkout_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("Checkout date")
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name=_("Total price")
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Comments")
    )
    number_guests = models.IntegerField(_("Number of guests"))
    advert = models.ForeignKey(
        Advert,
        on_delete=models.CASCADE,
        verbose_name=_("Advert")
    )

    def __str__(self):
        return f'{self.code} {self.price}'

    def clean(self, *args, **kwargs):
        if not self.checkin_date and self.checkout_date:
            raise ValidationError(
                _("Checkout need checkin"),
            )

        if self.checkin_date and self.checkout_date:
            if self.checkin_date > self.checkout_date:
                raise ValidationError(
                    _("Checkout must occur after checkin"),
                )
        super().clean()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self. code:
            self.code = get_random_string(length=20)
            while True:
                try:
                    return super(Reservation, self).save(force_insert, force_update, using, update_fields)
                except Exception:
                    self.code = get_random_string(length=20)
        return super(Reservation, self).save(force_insert, force_update, using, update_fields)
