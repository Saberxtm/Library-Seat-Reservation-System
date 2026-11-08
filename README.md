# Library Seat Reservation System

## 1. Project Overview

The Library Seat Reservation System is a web-based application that helps university students find and reserve available study seats in the library.

Students can check seat availability, make reservations, view upcoming bookings, and cancel reservations. Library staff can manage seat availability and view reservation information.

## 2. Problem Statement

Students may waste time searching for available study spaces, especially during busy library hours. The system provides a way to check seat availability and reserve a seat for a specific time period.

## 3. Main Functional Requirements

- View available seats for a selected time period.
- Reserve an available seat.
- Prevent overlapping reservations for the same seat.
- View current and upcoming reservations.
- Cancel an upcoming reservation.
- Allow authorized library staff to manage seat availability.
- Authenticate users through the university authentication service.

## 4. Architecture

The project uses **Layered Architecture**.

| Layer / Container | Technology | Responsibility |
|---|---|---|
| Presentation | React | User interface |
| Business Logic | Python, FastAPI | Reservation rules and request handling |
| Data Storage | PostgreSQL | Seat and reservation records |

The backend integrates with the university authentication service to verify user identity and roles.

## 5. Repository Structure

```text
Library-Seat-Reservation-System/
├── frontend/
│   └── README.md
├── backend/
│   └── README.md
├── docs/
│   ├── ADR-001.md
│   └── container-diagram.md
└── README.md
```

## 6. Architecture Documentation

- [Container Diagram](docs/container-diagram.md)
- [ADR-001: Layered Architecture](docs/ADR-001.md)

## 7. Team Members

| Member | Student ID | Contribution |
|---|---|---|
| Dias | 240107070 | Problem definition and requirements |
| Kazbekbi | 240107060 | Container diagram |
| Yerassyl | 240107092 | Architecture decision record |
| Assylbek | 240107068 | Repository and documentation |

## 8. Project Status

**Milestone 1:** Project scope and requirements defined.

**Milestone 2:** Initial architecture documentation and repository structure prepared.

## 9. Milestone 3 - Working Prototype

### Implemented Feature
The team implemented a Library Seat Reservation API
using Python, FastAPI, SQLAlchemy, and PostgreSQL.

Students can:
- View library seats.
- Create a seat reservation.
- View existing reservations.

The system:
- Rejects reservations for nonexistent seats.
- Prevents duplicate bookings for the same
  seat, date, and time slot.
- Saves reservations in PostgreSQL.

### Design Pattern
We implemented the Repository pattern.

- main.py handles API requests.
- services.py contains business rules.
- repository.py handles database operations.
- models.py defines the database table.
- database.py configures PostgreSQL.

The Repository pattern separates business logic
from database operations and makes testing easier.

### How to Run

1. Open a terminal in the backend folder.
2. Activate the Python virtual environment.
3. Install dependencies.
4. Configure the local PostgreSQL database.
5. Create the database tables.
6. Start the FastAPI server.

Commands:

    pip install fastapi "uvicorn[standard]" sqlalchemy "psycopg[binary]" pytest httpx

    python create_tables.py

    python -m uvicorn main:app --reload

API documentation:
http://127.0.0.1:8000/docs

### Automated Testing

Run:

    python -m pytest tests/ -v

Three automated tests:
1. Successful seat reservation.
2. Invalid seat rejection.
3. Double-booking prevention.

All three unit tests passed.

### Architecture Documentation

Updated documents:
- Milestone 3 container diagram
- Reservation component diagram
- ADR-002: Repository Pattern

ADR-001 remains accepted.
The selected architecture remains Layered Architecture.

### Limitations

The prototype currently supports exact time slots,
not arbitrary overlapping time intervals.

The frontend and university authentication
integration are outside the implemented prototype.

The database concurrency guarantee requires
a separate PostgreSQL integration test.

### AI Use Disclosure

AI assisted with explaining FastAPI, proposing
repository separation, helping with code fixes,
and suggesting automated tests.Moreover AI used for writing texts
