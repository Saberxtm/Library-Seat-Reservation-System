from database import engine, Base
from models import Reservation

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")
