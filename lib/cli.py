import inquirer
from geopy import distance, geocoders
from simple_chalk import green, blue, yellow, red

class DistanceCalculator:
    def __init__(self):
        # Transport modes with emojis and speeds
        self.transport_modes = [
            {"mode": "Walking", "emoji": "🚶", "speed": 5},  # Speed: 5 km/h
            {"mode": "Cycling", "emoji": "🚴", "speed": 15},  # Speed: 15 km/h
            {"mode": "Car", "emoji": "🚗", "speed": 80},  # Speed: 80 km/h
            {"mode": "Bus", "emoji": "🚌", "speed": 60},  # Speed: 60 km/h
            {"mode": "Train", "emoji": "🚆", "speed": 120},  # Speed: 120 km/h
            {"mode": "Airplane", "emoji": "🛬", "speed": 800}  # Speed: 800 km/h
        ]
        self.geolocator = geocoders.Nominatim(user_agent="distance_calculator")  # Geolocator instance

    def get_city_input(self, prompt_text):
        """Prompt the user for city name and country."""
        city = inquirer.prompt([
            inquirer.Text('name', message=f'Enter the name of the {prompt_text} city: '),
            inquirer.Text('country', message=f'Enter the name of the {prompt_text} country: ')
        ])
        return city

    def geocode_city(self, city_data):
        """Convert city name and country to geographic coordinates."""
        location = f"{city_data['name']}, {city_data['country']}"
        try:
            return self.geolocator.geocode(location).point  # Returns a tuple of coordinates (lat, long, alt)
        except AttributeError:
            print(red(f"Error: Could not find coordinates for {location}. Please try again."))
            exit()

    def calculate_distance(self, coords1, coords2):
        """Calculate the distance between two sets of coordinates in km."""
        return distance.distance(coords1, coords2).km

    def display_results(self, city1, city2, walk_distance):
        """Display the results for all transport modes."""
        print(green('\nResults:'))
        print(f"Distance between {city1['name']}, {city1['country']} and {city2['name']}, {city2['country']}:\n")

        for transport in self.transport_modes:
            travel_time = walk_distance / transport["speed"]
            print(yellow(f" {transport['emoji']} {transport['mode']}: {walk_distance:.2f} km, time: {travel_time:.2f} hours"))

        # Additional Analysis
        print(blue("\nAdditional Analysis:"))
        print(f"The shortest time is {walk_distance / 800:.2f} hours by Airplane.")
        print(f"The longest time is {walk_distance / 5:.2f} hours by Walking.")

    def run(self):
        """Main method to execute the program."""
        print(blue('Welcome to the Distance Calculator!\n'))
        print(green("This tool calculates the distance between two cities and provides travel times for multiple transport modes.\n"))

        # Get input for two cities
        city1 = self.get_city_input("first")
        city2 = self.get_city_input("second")

        # Geocode the cities into coordinates
        coords1 = self.geocode_city(city1)
        coords2 = self.geocode_city(city2)

        # Calculate the walking distance
        walk_distance = self.calculate_distance(coords1, coords2)

        # Display the results
        self.display_results(city1, city2, walk_distance)

# Instantiate the class and run the program
if __name__ == "__main__":
    calculator = DistanceCalculator()
    calculator.run()
