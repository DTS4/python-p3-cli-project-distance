## Distance Calculator CLI 🚀

A feature-rich and interactive command-line application that calculates distances between two cities, estimates travel times across various modes of transport, and records trips in a database. Built using Python, SQLAlchemy, Geopy, and Inquirer, this tool is ideal for quickly planning travel logistics or logging trip details.

## Features
Accurate Distance Calculation: Calculates the distance in kilometres between two cities using geocoding.
Multiple Transport Modes: Provides estimated travel times for:
🚶 Walking
🚗 Car
✈️ Airplane
User and Trip Management:
Store user information (name, email).
Log trips, including start and destination cities, distance, and date.
Persistent Data Storage:
Uses SQLite to manage user, city, and trip data.
Interactive Prompts: Easy-to-follow command-line input powered by Inquirer.
Error Handling: Handles invalid inputs or missing city coordinates gracefully.

## How to Run
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd <repository-folder>
Install the Required Dependencies:
Ensure Python 3.8+ is installed, then run:

bash
Copy code
pip install -r requirements.txt
Run the Program:
Execute the CLI tool:

bash
Copy code
python lib/cli.py
Example Usage:

Follow the prompts to input user details, start city, and destination city.
Example cities:
Start: Nairobi, Kenya
End: Mombasa, Kenya
Output will include:

yaml
Copy code
Distance between Nairobi, Kenya and Mombasa, Kenya:
🚶 Walking: 482.40 km, time: 96.48 hours
🚗 Car: 482.40 km, time: 6.03 hours
✈️ Airplane: 482.40 km, time: 0.60 hours
View the Database:
Open the travel_app.db file with any SQLite viewer (e.g., DB Browser for SQLite) to inspect stored users, trips, and cities.

## Dependencies
Python 3.8+
SQLAlchemy
Geopy
Inquirer
Simple Chalk
## Project Structure
bash
Copy code
project-folder/  
│  
├── lib/  
│   └── cli.py            # Main application file  
├── travel_app.db         # SQLite database (created after running)  
└── requirements.txt      # Project dependencies  
## Contributing
Feel free to fork, submit issues, or create pull requests to improve the project. Contributions are always welcome!