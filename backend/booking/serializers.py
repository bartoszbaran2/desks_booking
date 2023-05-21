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
        fields = ("id", "desk_number")


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = models.Reservation
        fields = ("user", "desk", "reservation_date", "date_reserved")
