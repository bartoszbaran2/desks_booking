from rest_framework.serializers import ModelSerializer
from . import models


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = models.Department
        fields = (
            "id",
            "name",
        )


class DeskSerializer(ModelSerializer):
    class Meta:
        model = models.Desk
        fields = ("id", "desk_code")


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ("id", "name", "username")


class ReservationSerializer(ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = models.Reservation
        fields = ("id", "employee", "desk", "reservation_date", "date_reserved")
