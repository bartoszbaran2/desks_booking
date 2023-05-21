from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Desk(models.Model):
    department = models.ForeignKey("Department", on_delete=models.CASCADE, related_name="desks")
    desk_code = models.CharField(editable=False)

    def __str__(self):
        return self.desk_code

    def generate_desk_code(self):
        """Generates a unique desk id based on the current amount of desk in given department and department name
        :rtype: str
        """
        desks_in_department = Desk.objects.filter(department=self.department).count()
        desk_code = f"{self.department.name}0{desks_in_department + 1}"
        return desk_code

    def save(self, *args, **kwargs):
        if not self.desk_code:
            self.desk_code = self.generate_desk_code()
        super().save(*args, **kwargs)


class Reservation(models.Model):
    employee = models.ForeignKey("Employee", on_delete=models.DO_NOTHING, related_name="reservations")
    desk = models.ForeignKey("Desk", on_delete=models.CASCADE, related_name="reservations")
    reservation_date = models.DateField()
    date_reserved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.employee} | Date:{self.reservation_date}"


class Employee(models.Model):
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=8)
    department = models.ForeignKey("Department", on_delete=models.DO_NOTHING, related_name="employees")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.username = self.username.upper()
        self.name = self.name.capitalize()
        super().save(*args, **kwargs)
