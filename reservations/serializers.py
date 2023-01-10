from rest_framework import serializers

from reservations.models import Reservation


class CreateReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = (
            'checkin_date',
            'checkout_date',
            'price',
            'comment',
            'number_guests',
            'advert'
        )

    def validate(self, data):
        checkin_date = data.get('checkin_date') or None
        checkout_date = data.get('checkout_date') or None
        if checkout_date and not checkin_date:
            raise serializers.ValidationError("Checkout need checkin")

        if checkout_date and checkin_date:
            if checkout_date < checkin_date:
                raise serializers.ValidationError("Checkout must occur after checkin")
        return data


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'
