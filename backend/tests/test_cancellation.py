from datetime import datetime, timezone
from events import EventBus, ReservationCancelled, ReservationCreated
from consumers import CancellationConsumer, NotificationConsumer
from services import ReservationService


class FakeRepository:

    def __init__(self):
        self.reservations = [
            {
                "id": 1,
                "student_id": 10,
                "seat_id": 2
            }
        ]

    def delete(self, reservation_id):
        for reservation in self.reservations:
            if reservation["id"] == reservation_id:
                self.reservations.remove(reservation)
                return reservation

        raise ValueError("Reservation not found")


def test_successful_cancellation():
    repository = FakeRepository()
    bus = EventBus()
    consumer = CancellationConsumer()
    confirmation = NotificationConsumer()

    bus.subscribe(consumer, ReservationCancelled)
    bus.subscribe(confirmation, ReservationCreated)

    service = ReservationService(repository, bus)

    result = service.cancel(1)

    assert result["id"] == 1
    assert len(repository.reservations) == 0
    assert len(consumer.processedEvents) == 1
    assert len(consumer.notifications) == 1
    assert consumer.notifications[0]["studentId"] == 10
    assert consumer.notifications[0]["reservationId"] == 1
    assert len(confirmation.notifications) == 0


def test_duplicate_cancellation_event():
    bus = EventBus()
    consumer = CancellationConsumer()

    bus.subscribe(consumer, ReservationCancelled)

    event = ReservationCancelled(
        eventId="cancel-001",
        reservationId=1,
        studentId=10,
        occurredAt=datetime.now(timezone.utc)
    )

    bus.publish(event)
    bus.publish(event)

    assert len(consumer.notifications) == 1
    assert len(consumer.processedEvents) == 1