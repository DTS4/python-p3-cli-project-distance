from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime
import inquirer
from geopy import distance, geocoders
from simple_chalk import green, blue, yellow, red

# SQLAlchemy Base
Base = declarative_base()

# Database Models
class User(Base):
    """User table."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    trips = relationship("Trip", back_populates="user")

class City(Base):
    """City table."""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)

    trips_start = relationship("Trip", foreign_keys="[Trip.start_city_id]", back_populates="start_city")
    trips_end = relationship("Trip", foreign_keys="[Trip.end_city_id]", back_populates="end_city")

class Trip(Base):
    """Trip table."""
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    start_city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    end_city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    distance_km = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="trips")
    start_city = relationship("City", foreign_keys=[start_city_id], back_populates="trips_start")
    end_city = relationship("City", foreign_keys=[end_city_id], back_populates="trips_end")

# Database Setup
engine = create_engine("sqlite:///travel_app.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Application Class
class DistanceCalculator:
    def __init__(self):
        self.transport_modes = [
            {"mode": "Walking", "emoji": "🚶", "speed": 5},
            {"mode": "Cycling", "emoji": "🚴", "speed": 15},
            {"mode": "Car", "emoji": "🚗", "speed": 80},
            {"mode": "Bus", "emoji": "🚌", "speed": 60},
            {"mode": "Train", "emoji": "🚆", "speed": 120},
            {"mode": "Airplane", "emoji": "🛬", "speed": 800},
        ]
        self.geolocator = geocoders.Nominatim(user_agent="distance_calculator")

    def get_user(self):
        """Prompt user for their details."""
        name = input("Enter your name: ")
        email = input("Enter your email: ")

        # Check if user exists, otherwise create
        user = session.query(User).filter_by(email=email).first()
        if not user:
            user = User(name=name, email=email)
            session.add(user)
            session.commit()
            print(green("User added successfully!\n"))
        return user

    def get_city_input(self, prompt_text):
        """Prompt the user for city name and country."""
        city = inquirer.prompt([
            inquirer.Text('name', message=f'Enter the name of the {prompt_text} city: '),
            inquirer.Text('country', message=f'Enter the name of the {prompt_text} country: ')
        ])

        # Check if city exists in the database
        db_city = session.query(City).filter_by(name=city['name'], country=city['country']).first()
        if not db_city:
            db_city = City(name=city['name'], country=city['country'])
            session.add(db_city)
            session.commit()
            print(green(f"City {city['name']}, {city['country']} added to the database.\n"))
        return db_city

    def geocode_city(self, city):
        """Geocode a city using its name and country."""
        location = f"{city.name}, {city.country}"
        try:
            return self.geolocator.geocode(location).point
        except AttributeError:
            print(red(f"Error: Could not find coordinates for {location}. Please try again."))
            exit()

    def calculate_distance(self, coords1, coords2):
        """Calculate the distance between two sets of coordinates in km."""
        return distance.distance(coords1, coords2).km

    def record_trip(self, user, start_city, end_city, distance_km):
        """Record a trip in the database."""
        trip = Trip(user_id=user.id, start_city_id=start_city.id, end_city_id=end_city.id, distance_km=distance_km)
        session.add(trip)
        session.commit()
        print(green("Trip recorded successfully!\n"))

    def display_results(self, start_city, end_city, distance_km):
        """Display the results for all transport modes."""
        print(blue(f"\nDistance between {start_city.name}, {start_city.country} and {end_city.name}, {end_city.country}:\n"))

        for mode in self.transport_modes:
            time = distance_km / mode["speed"]
            print(yellow(f" {mode['emoji']} {mode['mode']}: {distance_km:.2f} km, time: {time:.2f} hours"))

    def run(self):
        """Main method to execute the program."""
        print(blue("Welcome to the Distance Calculator!\n"))

        # Get user
        user = self.get_user()

        # Get input for start and end cities
        start_city = self.get_city_input("start")
        end_city = self.get_city_input("end")

        # Geocode cities
        coords1 = self.geocode_city(start_city)
        coords2 = self.geocode_city(end_city)

        # Calculate distance
        distance_km = self.calculate_distance(coords1, coords2)

        # Display results
        self.display_results(start_city, end_city, distance_km)

        # Record trip
        self.record_trip(user, start_city, end_city, distance_km)

# Instantiate and run the calculator
if __name__ == "__main__":
    calculator = DistanceCalculator()
    calculator.run()
