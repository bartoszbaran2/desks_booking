from datetime import datetime

import pytest
from booking.models import Department, Desk, Reservation


@pytest.fixture
def user(db, django_user_model):
    return django_user_model.objects.create_user(username="test_user", password="test_password", email="test@test.com")


@pytest.fixture
def department(db):
    return Department.objects.create(name="test_department")


@pytest.fixture
def desk(department, db):
    return Desk.objects.create(department=department)


@pytest.fixture
def reservation(user, desk, db):
    return Reservation.objects.create(
        user=user, desk=desk, reservation_date=datetime.today(), date_reserved=datetime.now()
    )
