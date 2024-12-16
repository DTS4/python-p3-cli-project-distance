import inquirer
from geopy import distance, geocoders
from simple_chalk import green, blue, yellow

# Define emojis for different modes
walking_emoji = "🚶"
bus_emoji = "🚌"
plane_emoji = "🛬"

# Display a welcome message
print(blue('Welcome to the distance calculator!\n'))

# Use inquirer to prompt the user for the first city's name and country
first_city = inquirer.prompt([
    inquirer.Text('name', message='Enter the name of the first city: '),
    inquirer.Text('country', message='Enter the name of the first country: ')
])

# Prompt the user for the second city's name and country
second_city = inquirer.prompt([
    inquirer.Text('name', message='Enter the name of the second city: '),
    inquirer.Text('country', message='Enter the name of the second country: ')
])

# Initialize the geolocator for geocoding city names into coordinates
geolocator = geocoders.Nominatim(user_agent="distance_calculator")

# Combine the city's name and country into a single string and geocode it into coordinates (latitude, longitude, altitude)
first_city_data = (
    first_city['name'],  # City name
    first_city['country'],  # Country name
    geolocator.geocode(f"{first_city['name']}, {first_city['country']}").point  # Coordinates as a tuple
)

second_city_data = (
    second_city['name'],
    second_city['country'],
    geolocator.geocode(f"{second_city['name']}, {second_city['country']}").point
)