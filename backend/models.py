from sqlalchemy import Column, Integer, String, UniqueConstraint
from database import Base


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, nullable=False)
    seat_id = Column(Integer, nullable=False)
    date = Column(String, nullable=False)
    time = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "seat_id", "date", "time",
            name="unique_seat_booking"
        ),
    )
