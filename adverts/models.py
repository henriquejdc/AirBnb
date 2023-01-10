from django.db import models
from django.utils.translation import gettext_lazy as _

from properties.models import Property
from shared.models import BaseModelDate


# Create your models here.
class Advert(BaseModelDate):
    platform = models.CharField(max_length=100, verbose_name=_("Platform"))
    platform_tax = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name=_("Platform tax")
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        verbose_name=_("Property")
    )

    def __str__(self):
        return f'{self.platform} V: {self.platform_tax} P: {self.property}'
