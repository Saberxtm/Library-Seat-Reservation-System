from datetime import datetime, timezone
from events import EventBus, ReservationCreated
from consumers import NotificationConsumer
from services import ReservationService


class FakeRepository:

    def __init__(self):
        self.reservations = []

    def get_all(self):
        return self.reservations

    def save(self, reservation):
        result = reservation.copy()
        result["id"] = 1
        self.reservations.append(result)
        return result


def test_successful_reaction():
    repository = FakeRepository()
    bus = EventBus()
    consumer = NotificationConsumer()

    bus.subscribe(consumer)

    service = ReservationService(repository, bus)

    seats = [{"id": 1, "number": 101}]

    reservation = {
        "student_id": 10,
        "seat_id": 1,
        "date": "2026-11-24",
        "time": "12:00"
    }

    result = service.create(reservation, seats)

    assert result["id"] == 1
    assert len(repository.reservations) == 1
    assert len(consumer.processedEvents) == 1
    assert len(consumer.notifications) == 1
    assert consumer.notifications[0]["studentId"] == 10
    assert consumer.notifications[0]["reservationId"] == 1


def test_duplicate_delivery():
    bus = EventBus()
    consumer = NotificationConsumer()

    bus.subscribe(consumer)

    event = ReservationCreated(
        eventId="event-001",
        reservationId=1,
        studentId=10,
        occurredAt=datetime.now(timezone.utc)
    )

    bus.publish(event)
    bus.publish(event)

    assert len(consumer.notifications) == 1
    assert len(consumer.processedEvents) == 1