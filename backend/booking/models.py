from django.contrib.auth import get_user_model
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Desk(models.Model):
    department = models.ForeignKey("Department", on_delete=models.CASCADE, related_name="desks")

    def __str__(self):
        return self.department.name[:5] + str(self.id)


class Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, related_name="reservations")
    desk = models.ForeignKey("Desk", on_delete=models.CASCADE, related_name="reservations")
    reservation_date = models.DateField(null=True, blank=True)
    date_reserved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user.username} | Date:{self.reservation_date}"
