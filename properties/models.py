from django.db import models
from django.utils.translation import gettext_lazy as _

from shared.models import BaseModelDate


# Create your models here.
class Property(BaseModelDate):
    activated_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("Activated date")
    )
    cleaning_value = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name=_("Cleaning value")
    )
    accepts_animals = models.BooleanField(
        default=False, verbose_name=_("Accept animals?"))
    max_number_guests = models.IntegerField(_("Max. Number of guests"))
    bathrooms = models.IntegerField(_("Bathroomss"))

    def __str__(self):
        return f'Code {self.id} G: {self.max_number_guests} B:{self.bathrooms}'
