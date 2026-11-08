# ADR-002: Repository Pattern for Seat Reservations

Status: Accepted

## Context
The Library Seat Reservation System must validate
reservations, prevent double bookings, and store
reservation information in PostgreSQL.

Putting validation rules and database operations
inside API endpoints would make the system harder
to test and maintain.

## Decision
We use the Repository pattern for reservation
data access.

ReservationService contains business rules.

ReservationRepository uses SQLAlchemy to read
and save reservations in PostgreSQL.

The repository is passed to the service through
constructor injection.

## Alternatives Considered
Direct database access from FastAPI endpoints.

This would require fewer classes but would
couple HTTP handling, business rules, and
database operations.

## Positive Consequences
- Clear separation of responsibilities.
- Business logic can be tested independently.
- Fake repositories can replace PostgreSQL in tests.
- Database implementation can change more easily.

## Negative Consequences
- More files and classes.
- Additional abstraction for a small project.
- Database integration still requires separate tests.