from geopy import geocoders
from simple_chalk import red

geolocator = geocoders.Nominatim(user_agent="distance_calculator")

def geocode_city(city_name, country_name):
    """Geocode a city and return coordinates."""
    location = f"{city_name}, {country_name}"
    try:
        return geolocator.geocode(location).point
    except AttributeError:
        print(red(f"Error: Could not find coordinates for {location}."))
        return None
