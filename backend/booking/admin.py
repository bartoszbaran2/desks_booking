from django.contrib import admin
from . import models


class ReservationAdminConfig(admin.ModelAdmin):
    list_display = ("employee", "desk", "reservation_date", "date_reserved")
    list_editable = ("desk", "reservation_date")
    list_filter = ("employee", "desk", "reservation_date")
    save_on_top = True
    list_per_page = 50


class EmployeeAdminConfig(admin.ModelAdmin):
    list_display = ("name", "username", "department")


admin.site.register(models.Department)
admin.site.register(models.Desk)
admin.site.register(models.Reservation, ReservationAdminConfig)
admin.site.register(models.Employee, EmployeeAdminConfig)
