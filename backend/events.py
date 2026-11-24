from dataclasses import dataclass
from datetime import datetime


@dataclass
class ReservationCreated:
    eventId: str
    reservationId: int
    studentId: int
    occurredAt: datetime


@dataclass
class ReservationCancelled:
    eventId: str
    reservationId: int
    studentId: int
    occurredAt: datetime


class EventBus:
    def __init__(self):
        self.consumers = []

    def subscribe(self, consumer, event_type=None):
        self.consumers.append((consumer, event_type))

    def publish(self, event):
        for consumer, event_type in self.consumers:
            if event_type is None or isinstance(event, event_type):
                consumer.handle(event)