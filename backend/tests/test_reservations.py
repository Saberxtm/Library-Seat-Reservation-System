import pytest
from services import ReservationService


# Fake repository for testing
class FakeRepository:
    def __init__(self):
        self.reservations = []

    def get_all(self):
        return self.reservations

    def save(self, reservation):
        saved = reservation.copy()
        saved["id"] = len(self.reservations) + 1
        self.reservations.append(saved)
        return saved


# Test 1: Successful reservation
def test_successful_reservation():
    repo = FakeRepository()
    service = ReservationService(repo)

    seats = [{"id": 1, "number": 101}]

    reservation = {
        "student_id": 123,
        "seat_id": 1,
        "date": "2026-11-12",
        "time": "10:00"
    }

    result = service.create(reservation, seats)

    assert result["seat_id"] == 1
    assert len(repo.get_all()) == 1


# Test 2: Invalid seat
def test_invalid_seat():
    repo = FakeRepository()
    service = ReservationService(repo)

    seats = [{"id": 1, "number": 101}]

    reservation = {
        "student_id": 123,
        "seat_id": 999,
        "date": "2026-11-12",
        "time": "10:00"
    }

    with pytest.raises(ValueError, match="Seat not found"):
        service.create(reservation, seats)

    assert len(repo.get_all()) == 0


# Test 3: Prevent double booking
def test_double_booking():
    repo = FakeRepository()
    service = ReservationService(repo)

    seats = [{"id": 1, "number": 101}]

    reservation = {
        "student_id": 123,
        "seat_id": 1,
        "date": "2026-11-12",
        "time": "10:00"
    }

    service.create(reservation.copy(), seats)

    with pytest.raises(ValueError, match="Seat is already reserved"):
        service.create(reservation.copy(), seats)

    assert len(repo.get_all()) == 1
