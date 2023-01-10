import json
from typing import List

from django.urls import reverse
from model_bakery import baker
from rest_framework import status

from reservations.serializers import ReservationSerializer
from shared.tests import BaseAPITestCase


class ReservationViewSetViewSetTestCase(BaseAPITestCase):
    """Test all scenarios for ReservationViewSetViewSet."""

    tests_to_perform: List = [
        'create_ok',
        'create_validation_error',
        'list',
        'retrieve',
        'destroy_http_404',
        'destroy_ok',
    ]

    def setUp(self) -> None:
        super().setUp()
        self.url = reverse("reservation-list")
        self.test_protected_error = False
        self.validation_error_column = 'price'
        property = baker.make(
            "properties.Property",
            activated_date="2023-01-10T22:12:45.836Z",
            cleaning_value="130.00",
            accepts_animals=False,
            max_number_guests=1,
            bathrooms=1,
        )
        self.advert = baker.make(
            "adverts.Advert",
            platform="airbnb",
            platform_tax="30.00",
            property=property
        )
        self.row_object = baker.make(
            "reservations.Reservation",
            checkin_date="2023-01-10T22:57:21.760000Z",
            checkout_date="2023-01-10T22:57:21.760000Z",
            price="1000.00",
            comment='Teste',
            number_guests=2,
            advert=self.advert,
        )
        self.row_object2 = baker.make(
            "reservations.Reservation",
            checkin_date="2023-01-10T22:57:21.760000Z",
            checkout_date="2023-01-10T22:57:21.760000Z",
            price="1000.00",
            comment='Teste',
            number_guests=2,
            advert=self.advert,
        )
        self.row_object_no_relation = self.row_object

        self.post_data = {
          "checkin_date": "2023-01-10T22:57:21.760000Z",
          "checkout_date": "2023-01-10T22:57:21.760000Z",
          "price": "1220.00",
          "comment": "Teste",
          "number_guests": 2,
          "advert": self.advert.id
        }

        self.total_rows = 2
        self.http_404_error_description = "No Reservation matches the given query."

    def set_test_retrieve_fields(self):
        data = ReservationSerializer(self.row_object).data
        self.retrieve_test_fields = data

    def test_create_checkout_after_checkin(self):
        post_data = {
            "checkin_date": "2023-01-11T22:57:21.760000Z",
            "checkout_date": "2023-01-10T22:57:21.760000Z",
            "price": "1220.00",
            "comment": "Teste",
            "number_guests": 2,
            "advert": self.advert.id
        }
        response = self.post(
            self.url,
            data=post_data
        )
        contents = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(
            contents,
            {
                'status': 400,
                'error': 'ValidationError',
                'description': {'detail': {'errors': ['Checkout must occur after checkin']}}
            }
        )
        del post_data['checkin_date']
        response = self.post(
            self.url,
            data=post_data
        )
        contents = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(
            contents,
            {
                'status': 400,
                'error': 'ValidationError',
                'description': {'detail': {'errors': ['Checkout need checkin']}}
            }
        )
