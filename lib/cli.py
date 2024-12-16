import inquirer
from geopy import distance, geocoders
from simple_chalk import green, blue, yellow

# Define emojis for different modes
walking_emoji = "🚶"
bus_emoji = "🚌"
plane_emoji = "🛬"

# Display a welcome message
print(blue('Welcome to the distance calculator!\n'))