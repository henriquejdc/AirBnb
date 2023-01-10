from typing import List

from django.urls import reverse
from model_bakery import baker

from adverts.serializers import AdvertSerializer
from shared.tests import BaseAPITestCase


class AdvertViewSetViewSetTestCase(BaseAPITestCase):
    """Test all scenarios for AdvertViewSetViewSet."""

    tests_to_perform: List = [
        'create_ok',
        'create_validation_error',
        'update_ok',
        'update_validation_error',
        'update_http_404',
        'partial_update_ok',
        'partial_update_http_404',
        'list',
        'retrieve',
    ]

    def setUp(self) -> None:
        super().setUp()
        self.url = reverse("advert-list")
        self.test_protected_error = False
        self.validation_error_column = 'platform'
        property = baker.make(
            "properties.Property",
            activated_date='2023-01-10T22:12:45.836000Z',
            cleaning_value="130.00",
            accepts_animals=False,
            max_number_guests=1,
            bathrooms=1,
        )
        self.row_object = baker.make(
            "adverts.Advert",
            platform="airbnb",
            platform_tax="30.00",
            property=property
        )
        self.row_object2 = baker.make(
            "adverts.Advert",
            platform="mercado livre",
            platform_tax="10.00",
            property=property
        )
        self.row_object_no_relation = self.row_object

        self.post_data = {
          "platform": "airbnb",
          "platform_tax": "120.00",
          "property": property.id
        }

        self.total_rows = 2
        self.http_404_error_description = "No Advert matches the given query."

    def set_test_retrieve_fields(self):
        data = AdvertSerializer(self.row_object).data
        self.retrieve_test_fields = data
