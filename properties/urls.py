from django.urls import path
from rest_framework.routers import SimpleRouter

from properties.views import PropertyViewSet


router = SimpleRouter()
router.register(r'', PropertyViewSet, basename='property')
urlpatterns = router.urls
