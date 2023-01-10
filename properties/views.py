from properties.models import Property
from properties.serializers import PropertySerializer
from shared.views import BaseCollectionViewSet
from rest_framework.permissions import (
    IsAuthenticated
)


class PropertyViewSet(BaseCollectionViewSet):
    """ A ViewSet for retrieving Property. """
    model_class = Property
    queryset = model_class.objects.all()
    serializer_class = PropertySerializer
    serializers = {
        'default': serializer_class,
    }
    permission_classes = [IsAuthenticated]

