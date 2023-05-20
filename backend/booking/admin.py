from django.contrib import admin
from . import models


class ReservationAdminConfig(admin.ModelAdmin):
    list_display = ("user", "desk", "reservation_date", "date_reserved")
    list_editable = ("desk", "reservation_date")
    list_filter = ("user", "desk", "reservation_date")
    save_on_top = True
    list_per_page = 50


admin.site.register(models.Department)
admin.site.register(models.Desk)
admin.site.register(models.Reservation, ReservationAdminConfig)
