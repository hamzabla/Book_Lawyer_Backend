from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from appointments.models import Appointment
from appointments.permissions import IsLawyer, IsAuthorOrNotView
from appointments.serializers import AppointmentSerializer


# Create your views here.

# class AppointmentList(generics.ListCreateAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer
#
#
# class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsLawyer
    ]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthenticated,
        IsAuthorOrNotView
    ]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointment.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)


class AppointmentDetailViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsLawyer,
        IsAuthorOrNotView,
    ]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)
