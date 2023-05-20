from django.contrib.auth import get_user_model
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Desk(models.Model):
    department = models.ForeignKey("Department", on_delete=models.CASCADE, related_name="desks")
    desk_number = models.CharField(editable=False)

    def __str__(self):
        return self.desk_number

    def generate_desk_number(self):
        """Generates a unique desk id based on the current amount of desk in given department and department name
        :rtype: str
        """
        desks_in_department = Desk.objects.filter(department=self.department).count()
        desk_number = f"{self.department.name}0{desks_in_department + 1}"
        return desk_number

    def save(self, *args, **kwargs):
        if not self.desk_number:
            self.desk_number = self.generate_desk_number()
        super().save(*args, **kwargs)


class Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, related_name="reservations")
    desk = models.ForeignKey("Desk", on_delete=models.CASCADE, related_name="reservations")
    reservation_date = models.DateField(null=True, blank=True)
    date_reserved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user.username} | Date:{self.reservation_date}"
