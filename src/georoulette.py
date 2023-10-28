import geopandas as gpd
from geopy.distance import geodesic
from shapely.geometry import Point

def find_nearest_country(latitude, longitude, DATA_path):
    # Load border data from the shp file
    gdf = gpd.read_file(DATA_path)

    # Calculate the distance between the given coordinates and the borders of each country
    distances = gdf.geometry.apply(lambda geom: geodesic((latitude, longitude), (geom.centroid.y, geom.centroid.x)).km)

    # Find the index of the minimum distance
    nearest_idx = distances.idxmin()

    # Get the name of the country corresponding to the index of the minimum distance
    nearest_country = gdf.loc[nearest_idx].ADMIN

    # Display the name of the nearest country
    print(f"The nearest country is: {nearest_country}")

    return nearest_country

def find_country(latitude, longitude, DATA_path):
    # Load border data from the shp file
    gdf = gpd.read_file(DATA_path)

    # Create a point geometry for the given point
    point = Point(longitude, latitude)

    # Find the country that contains the point
    contains_point = gdf.geometry.contains(point)

    if contains_point.any():
        # The point is contained in at least one country
        country = gdf[contains_point].iloc[0]['ADMIN']
        return True, country
    else:
        # The point is not contained in any country
        return False, None

def find_closest_country(latitude, longitude, data_path):
    """
    Find the closest country based on the given geographical coordinates.

    Args:
        latitude (float): Latitude of the point.
        longitude (float): Longitude of the point.
        data_path (str): Path to the geographical data file.

    Returns:
        str: Name of the closest country.
    """
    # Find the name of the country in which the point is located
    country = find_country(latitude, longitude, data_path)

    # If the point is in the sea, find the nearest country
    if not country[0]:
        nearest_country = find_nearest_country(latitude, longitude, data_path)
        return nearest_country

    return country[1]
