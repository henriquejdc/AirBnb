from reservations.models import Reservation
from reservations.serializers import ReservationSerializer, CreateReservationSerializer
from shared.views import BaseCollectionViewSet
from rest_framework.permissions import (
    IsAuthenticated
)


class ReservationViewSet(BaseCollectionViewSet):
    """ A ViewSet for retrieving Reservation. """
    model_class = Reservation
    queryset = model_class.objects.all()
    serializer_class = ReservationSerializer
    http_method_names = ('get', 'post', 'delete')
    serializers = {
        'default': serializer_class,
        'create': CreateReservationSerializer
    }
    permission_classes = [IsAuthenticated]

