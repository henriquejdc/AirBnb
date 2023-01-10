from django.urls import path
from rest_framework.routers import SimpleRouter

from adverts.views import AdvertViewSet


router = SimpleRouter()
router.register(r'', AdvertViewSet, basename='advert')
urlpatterns = router.urls
