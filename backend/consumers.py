class NotificationConsumer:
    def __init__(self):
        self.notifications = []
        self.processedEvents = set()

    def handle(self, event):
        if event.eventId in self.processedEvents:
            return

        self.notifications.append({
            "studentId": event.studentId,
            "reservationId": event.reservationId,
            "message": "Your reservation is confirmed"
        })

        self.processedEvents.add(event.eventId)