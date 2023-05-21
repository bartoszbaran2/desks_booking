from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views, viewsets

app_name = "booking"

router = DefaultRouter()
router.register(r"reservations", viewsets.ReservationViewSet, basename="reservation-view-set")


urlpatterns = [
    path("departments/", views.DepartmentListView.as_view(), name="departments"),
    path("departments/<int:pk>/desks/", views.DeskListView.as_view(), name="desks-list"),
    path("departments/<int:pk>/employees/", views.EmployeeListView.as_view(), name="employees-list"),
    *router.urls,
]
