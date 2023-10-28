from shapely.geometry import Point
import geopandas as gpd
import matplotlib.pyplot as plt

def plot_country_borders(latitude, longitude, DATA_path, closest_country=None):
    # Load border data from the shp file
    gdf = gpd.read_file(DATA_path)

    point = Point(longitude, latitude)
    # Create a geospatial dataframe for the given point
    point_df = gpd.GeoDataFrame(geometry=[point])

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot country borders
    gdf.plot(ax=ax, edgecolor='gray', facecolor='black')

    # Color the closest country if specified
    if closest_country:
        country_gdf = gdf[gdf['ADMIN'] == closest_country]
        country_gdf.plot(ax=ax, edgecolor='black', facecolor='green')

    # Plot the given point
    point_df.plot(ax=ax, color='red', markersize=50)

    # Display the coordinates of the point in the figure title
    ax.set_title(f"Latitude: {latitude:.4f}, Longitude: {longitude:.4f}")

    # Show the figure
    plt.show()
