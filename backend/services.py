class ReservationService:

    def __init__(self, repository):
        self.repository = repository

    def create(self, reservation, seats):

        # Check if the seat exists
        seat_exists = False

        for seat in seats:
            if seat["id"] == reservation["seat_id"]:
                seat_exists = True

        if not seat_exists:
            raise ValueError("Seat not found")

        # Check if the seat is already booked
        for existing in self.repository.get_all():
            if (
                existing["seat_id"] == reservation["seat_id"]
                and existing["date"] == reservation["date"]
                and existing["time"] == reservation["time"]
            ):
                raise ValueError("Seat is already reserved")

        # Save to the database
        return self.repository.save(reservation)
