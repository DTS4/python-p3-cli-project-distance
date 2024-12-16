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
    first_city['name'],   
    first_city['country'],   
    geolocator.geocode(f"{first_city['name']}, {first_city['country']}").point   
)

second_city_data = (
    second_city['name'],
    second_city['country'],
    geolocator.geocode(f"{second_city['name']}, {second_city['country']}").point
)

# Calculate the distance in kilometres between the two sets of coordinates
walk_distance = distance.distance(first_city_data[2], second_city_data[2]).km

# Define a list of transport modes, their emojis, and speeds (in km/h)
transport_modes = [
    {"mode": "Walking", "emoji": walking_emoji, "speed": 5},  # Walking speed: 5 km/h
    {"mode": "Bus", "emoji": bus_emoji, "speed": 60},  # Bus speed: 60 km/h
    {"mode": "Airplane", "emoji": plane_emoji, "speed": 800}  # Airplane speed: 800 km/h
]

# Display the results header
print(green('\nResults:'))
print(f"Distance between {first_city_data[0]}, {first_city_data[1]} and {second_city_data[0]}, {second_city_data[1]} by:\n")

# Loop through the transport modes and calculate the time for each mode
for transport in transport_modes:
    # Travel time is calculated as distance divided by speed
    travel_time = walk_distance / transport["speed"]    
    # Print the result for the current mode of transport
    print(yellow(f" {transport['emoji']} {transport['mode']}: {walk_distance:.2f} km, time: {travel_time:.2f} hours"))