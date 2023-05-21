from datetime import datetime

import pytest
from booking.models import Department, Desk, Reservation, Employee


@pytest.fixture
def department(db):
    return Department.objects.create(name="test_department")


@pytest.fixture
def employee(department, db):
    return Employee.objects.create(name="test_employee", username="TEST01", department=department)


@pytest.fixture
def desk(department, db):
    return Desk.objects.create(department=department)


@pytest.fixture
def reservation(employee, desk, db):
    return Reservation.objects.create(
        employee=employee, desk=desk, reservation_date=datetime.today(), date_reserved=datetime.now()
    )
