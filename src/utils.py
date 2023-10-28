import random
from geopy.distance import distance

def generate_coordinates():
    """
    Randomly generates a pair of latitude and longitude coordinates,
    then displays them in the form of °N or °W depending on their direction.

    Returns:
        Tuple of float: a pair of coordinates (latitude, longitude).
    """
    # Generate a random latitude between -90 and 90
    latitude = random.uniform(-90, 90)

    # Generate a random longitude between -180 and 180
    longitude = random.uniform(-180, 180)

    # Determine the direction of latitude (North or South)
    lat_direction = "N" if latitude >= 0 else "S"

    # Determine the direction of longitude (East or West)
    long_direction = "E" if longitude >= 0 else "W"

    # Display the coordinates with their direction
    print(f"Latitude: {abs(latitude):.4f}°{lat_direction}")
    print(f"Longitude: {abs(longitude):.4f}°{long_direction}")

    # Return the coordinates as a tuple
    return latitude, longitude

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculates the distance in kilometers between two coordinates (latitude, longitude)
    using the Haversine formula.

    Args:
        lat1 (float): Latitude of the first point.
        lon1 (float): Longitude of the first point.
        lat2 (float): Latitude of the second point.
        lon2 (float): Longitude of the second point.

    Returns:
        float: The distance in kilometers between the two points.
    """
    return distance((lat1, lon1), (lat2, lon2)).km
