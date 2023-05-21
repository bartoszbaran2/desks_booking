from booking.models import Desk


def test_correct_gui_representation(department, desk, reservation):
    assert str(department) == department.name
    assert str(desk) == desk.desk_number
    assert str(reservation) == f"User: {reservation.user.username} | Date:{reservation.reservation_date}"


def test_generate_desk_number_unique(department, db):
    desk1 = Desk.objects.create(department=department)
    desk2 = Desk.objects.create(department=department)

    assert desk1.desk_number != desk2.desk_number
    assert desk1.desk_number == "test_department01"
    assert desk2.desk_number == "test_department02"
    assert Desk.objects.count() == 2


def test_save__not_change_desk_number(department):
    desk = Desk(department=department, desk_number="001")

    desk.save()

    assert desk.desk_number == "001"
