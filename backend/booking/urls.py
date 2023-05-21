from django.urls import path

from . import views

app_name = "booking"

urlpatterns = [
    path("departments/", views.DepartmentListView.as_view(), name="departments"),
    path("departments/<int:pk>/desks/", views.DeskListView.as_view(), name="desks-list"),
]
