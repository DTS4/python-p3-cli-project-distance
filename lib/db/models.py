from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    trips = relationship("Trip", back_populates="user")

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    trips_start = relationship("Trip", foreign_keys="[Trip.start_city_id]", back_populates="start_city")
    trips_end = relationship("Trip", foreign_keys="[Trip.end_city_id]", back_populates="end_city")

class Trip(Base):
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
