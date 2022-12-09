from rest_framework import serializers

from appointments.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','customer','title','subject','date')
        model = Appointment