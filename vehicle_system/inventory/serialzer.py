from rest_framework import serializers
from .models import Vehicle , Booking
from datetime import date

class Vehicleserialzer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"

class Bookingserialzer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"