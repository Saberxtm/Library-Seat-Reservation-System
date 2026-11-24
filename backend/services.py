from uuid import uuid4
from datetime import datetime, timezone
from events import ReservationCreated, ReservationCancelled, EventBus


class ReservationService:

    def __init__(self, repository, event_bus=None):
        self.repository = repository
        self.event_bus = event_bus or EventBus()

    def create(self, reservation, seats):

        seat_exists = False

        for seat in seats:
            if seat["id"] == reservation["seat_id"]:
                seat_exists = True

        if not seat_exists:
            raise ValueError("Seat not found")

        for existing in self.repository.get_all():
            if (
                existing["seat_id"] == reservation["seat_id"]
                and existing["date"] == reservation["date"]
                and existing["time"] == reservation["time"]
            ):
                raise ValueError("Seat is already reserved")

        result = self.repository.save(reservation)

        event = ReservationCreated(
            eventId=str(uuid4()),
            reservationId=result["id"],
            studentId=reservation["student_id"],
            occurredAt=datetime.now(timezone.utc)
        )

        self.event_bus.publish(event)

        return result

    def cancel(self, reservation_id):

        result = self.repository.delete(reservation_id)

        event = ReservationCancelled(
            eventId=str(uuid4()),
            reservationId=result["id"],
            studentId=result["student_id"],
            occurredAt=datetime.now(timezone.utc)
        )

        self.event_bus.publish(event)

        return result