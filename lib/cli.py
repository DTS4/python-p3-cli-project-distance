import inquirer
from geopy import distance, geocoders
from simple_chalk import green, blue, yellow

# Define a class to handle the distance calculation logic
class DistanceCalculator:
    def __init__(self):
        # Emojis for transport modes
        self.transport_modes = [
            {"mode": "Walking", "emoji": "🚶", "speed": 5},  # Speed: 5 km/h
            {"mode": "Bus", "emoji": "🚌", "speed": 60},  # Speed: 60 km/h
            {"mode": "Airplane", "emoji": "🛬", "speed": 800}  # Speed: 800 km/h
        ]
        self.geolocator = geocoders.Nominatim(user_agent="distance_calculator")  # Geocoder instance

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
        return self.geolocator.geocode(location).point  # Returns a tuple of coordinates (lat, long, alt)

    def calculate_distance(self, coords1, coords2):
        """Calculate the distance between two sets of coordinates in km."""
        return distance.distance(coords1, coords2).km

    def display_results(self, city1, city2, walk_distance):
        """Display the results for all transport modes."""
        print(green('\nResults:'))
        print(f"Distance between {city1['name']}, {city1['country']} and {city2['name']}, {city2['country']} by:\n")

        for transport in self.transport_modes:
            travel_time = walk_distance / transport["speed"]
            print(yellow(f" {transport['emoji']} {transport['mode']}: {walk_distance:.2f} km, time: {travel_time:.2f} hours"))

    def run(self):
        """Main method to execute the program."""
        print(blue('Welcome to the distance calculator!\n'))

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
