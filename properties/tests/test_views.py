from typing import List

from django.urls import reverse
from model_bakery import baker

from properties.serializers import PropertySerializer
from shared.tests import BaseAPITestCase


class PropertyViewSetViewSetTestCase(BaseAPITestCase):
    """Test all scenarios for PropertyViewSetViewSet."""

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
        'destroy_http_404',
        'destroy_ok',
    ]

    def setUp(self) -> None:
        super().setUp()
        self.url = reverse("property-list")
        self.test_protected_error = False
        self.validation_error_column = 'bathrooms'
        self.row_object = baker.make(
            "properties.Property",
            activated_date="2023-01-10T22:12:45.836000Z",
            cleaning_value="130.00",
            accepts_animals=False,
            max_number_guests=1,
            bathrooms=1,
        )
        self.row_object = baker.make(
            "properties.Property",
            activated_date="2023-01-10T22:12:45.836000Z",
            cleaning_value="300.00",
            accepts_animals=False,
            max_number_guests=2,
            bathrooms=2,
        )
        self.row_object_no_relation = self.row_object

        self.post_data = {
            "activated_date": "2023-01-10T22:12:45.836000Z",
            "cleaning_value": "120.00",
            "accepts_animals": True,
            "max_number_guests": 3,
            "bathrooms": 1
        }
        self.total_rows = 2
        self.http_404_error_description = "No Property matches the given query."

    def set_test_retrieve_fields(self):
        data = PropertySerializer(self.row_object).data
        self.retrieve_test_fields = data
