from dataclasses import dataclass
from datetime import datetime


@dataclass
class ReservationCreated:
    eventId: str
    reservationId: int
    studentId: int
    occurredAt: datetime


class EventBus:
    def __init__(self):
        self.consumers = []

    def subscribe(self, consumer):
        self.consumers.append(consumer)

    def publish(self, event):
        for consumer in self.consumers:
            consumer.handle(event)