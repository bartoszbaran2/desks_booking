from booking.models import Desk


def test_correct_gui_representation(department, desk, reservation):
    assert str(department) == department.name
    assert str(desk) == desk.desk_code
    assert str(reservation) == f"User: {reservation.user.username} | Date:{reservation.reservation_date}"


def test_generate_desk_code_unique(department, db):
    desk1 = Desk.objects.create(department=department)
    desk2 = Desk.objects.create(department=department)

    assert desk1.desk_code != desk2.desk_code
    assert desk1.desk_code == "test_department01"
    assert desk2.desk_code == "test_department02"
    assert Desk.objects.count() == 2


def test_save__not_change_desk_code(department):
    desk = Desk(department=department, desk_code="001")

    desk.save()

    assert desk.desk_code == "001"
