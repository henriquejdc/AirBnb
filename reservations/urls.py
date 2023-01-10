from rest_framework.routers import SimpleRouter

from reservations.views import ReservationViewSet


router = SimpleRouter()
router.register(r'', ReservationViewSet, basename='reservation')
urlpatterns = router.urls
