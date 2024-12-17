from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.cli import Base   

# Debugging: Enable echo to see SQL queries in the console
engine = create_engine("sqlite:///travel_app.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Recreate tables for debugging purposes
def reset_database():
    print("Resetting database...")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Database reset complete.")

if __name__ == "__main__":
    reset_database()
