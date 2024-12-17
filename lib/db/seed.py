from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, City, Trip
from datetime import datetime

# Setup the database
engine = create_engine("sqlite:///travel_app.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Seed Users
def seed_users():
    users = [
        User(name="John Doe", email="john@example.com"),
        User(name="Jane Smith", email="jane@example.com"),
    ]
    session.add_all(users)
    session.commit()
    print("Seeded users.")

# Seed Cities
def seed_cities():
    cities = [
        City(name="Nairobi", country="Kenya"),
        City(name="Mombasa", country="Kenya"),
        City(name="New York", country="USA"),
        City(name="London", country="UK"),
    ]
    session.add_all(cities)
    session.commit()
    print("Seeded cities.")

# Seed Trips
def seed_trips():
    trips = [
        Trip(user_id=1, start_city_id=1, end_city_id=2, distance_km=500.0, date=datetime.utcnow()),
        Trip(user_id=2, start_city_id=3, end_city_id=4, distance_km=5500.0, date=datetime.utcnow()),
    ]
    session.add_all(trips)
    session.commit()
    print("Seeded trips.")

if __name__ == "__main__":
    seed_users()
    seed_cities()
    seed_trips()
    print("Database seeding complete.")
