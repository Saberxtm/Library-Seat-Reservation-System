
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from repository import ReservationRepository
from services import ReservationService

app = FastAPI()

seats = [
    {"id": 1, "number": 101},
    {"id": 2, "number": 102},
    {"id": 3, "number": 103}
]

repository = ReservationRepository()
service = ReservationService(repository)


class Reservation(BaseModel):
    student_id: int
    seat_id: int
    date: str
    time: str


@app.get("/")
def home():
    return {"message": "Library Seat Reservation System is running"}


@app.get("/seats")
def get_seats():
    return {"seats": seats}


@app.post("/reservations")
def create_reservation(reservation: Reservation):
    try:
        result = service.create(reservation.model_dump(), seats)
        return {
            "message": "Reservation created successfully",
            "reservation": result
        }
    except ValueError as error:
        if str(error) == "Seat not found":
            raise HTTPException(status_code=404, detail=str(error))
        raise HTTPException(status_code=409, detail=str(error))


@app.get("/reservations")
def get_reservations():
    return {"reservations": repository.get_all()}
