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
