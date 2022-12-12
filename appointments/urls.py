from rest_framework.routers import SimpleRouter

from appointments.views import AppointmentViewSet, CustomerViewSet, AppointmentDetailViewSet
from django.urls import path


router = SimpleRouter()
router.register("lawyer", AppointmentViewSet, basename="lawyers")
router.register("customer", CustomerViewSet, basename="customers")
router.register("<int:pk>", AppointmentDetailViewSet, basename="appointments")
urlpatterns = router.urls
