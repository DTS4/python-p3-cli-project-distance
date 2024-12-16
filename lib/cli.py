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