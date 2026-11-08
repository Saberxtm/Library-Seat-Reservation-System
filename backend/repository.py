from sqlalchemy.exc import IntegrityError
from models import Reservation
from database import SessionLocal


class ReservationRepository:

    def get_all(self):
        with SessionLocal() as db:
            reservations = db.query(Reservation).all()

            return [
                {
                    "id": r.id,
                    "student_id": r.student_id,
                    "seat_id": r.seat_id,
                    "date": r.date,
                    "time": r.time
                }
                for r in reservations
            ]

    def save(self, reservation):
        with SessionLocal() as db:
            new_reservation = Reservation(
                student_id=reservation["student_id"],
                seat_id=reservation["seat_id"],
                date=reservation["date"],
                time=reservation["time"]
            )

            db.add(new_reservation)

            try:
                db.commit()
            except IntegrityError:
                db.rollback()
                raise ValueError("Seat is already reserved")

            db.refresh(new_reservation)

            return {
                "id": new_reservation.id,
                "student_id": new_reservation.student_id,
                "seat_id": new_reservation.seat_id,
                "date": new_reservation.date,
                "time": new_reservation.time
            }
