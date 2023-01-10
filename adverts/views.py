from adverts.models import Advert
from adverts.serializers import AdvertSerializer
from shared.views import BaseCollectionViewSet
from rest_framework.permissions import (
    IsAuthenticated
)


class AdvertViewSet(BaseCollectionViewSet):
    """ A ViewSet for retrieving Advert. """
    model_class = Advert
    queryset = model_class.objects.all()
    serializer_class = AdvertSerializer
    http_method_names = ('get', 'post', 'put', 'patch')
    serializers = {
        'default': serializer_class,
    }
    permission_classes = [IsAuthenticated]
