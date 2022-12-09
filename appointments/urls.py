from rest_framework.routers import SimpleRouter

from appointments.views import AppointmentViewSet, CustomerViewSet, AppointmentDetailViewSet
from django.urls import path

# urlpatterns = [
#     path("<int:pk>/", AppointmentDetail.as_view()),
#     path("", AppointmentList.as_view())
# ]

router = SimpleRouter()

#router.register("",AppointmentViewSet, basename= "appointments")
router.register("lawyer",AppointmentViewSet,basename= "appointments_lawyer")
router.register("customer",CustomerViewSet,basename= "appointments_customer")
router.register("<int:pk>",AppointmentDetailViewSet,basename= "detail")

urlpatterns = router.urls
