from booking.models import Desk, Employee


def test_correct_gui_representation(department, desk, reservation, employee):
    assert str(department) == department.name
    assert str(desk) == desk.desk_code
    assert str(reservation) == f"User: {reservation.employee} | Date:{reservation.reservation_date}"
    assert str(employee) == employee.name


def test_generate_desk_code_unique(department, db):
    desk1 = Desk.objects.create(department=department)
    desk2 = Desk.objects.create(department=department)

    assert desk1.desk_code != desk2.desk_code
    assert desk1.desk_code == "test_department01"
    assert desk2.desk_code == "test_department02"
    assert Desk.objects.count() == 2


def test_save_not_change_desk_code(department):
    desk = Desk(department=department, desk_code="001")

    desk.save()

    assert desk.desk_code == "001"


def test_employee_field_lowercase(db, department):
    name = "test Name"
    username = "test"
    employee = Employee(name=name, username=username, department=department)

    employee.save()

    assert employee.username == username.upper()
    assert employee.name == name.capitalize()
