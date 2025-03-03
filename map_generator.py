import folium

from track_past_temp import get_past_summer_temp
from Location_to_lat_long import get_coordinates

def make_map(location):
    coord = get_coordinates(location)

    if coord:
        lat, long = coord
        temp = get_past_summer_temp(lat, long)
        if temp is None:
            print("Can't get the temperature ({temp})")
            return
        else:
            print(f"The coordinates of {location} is lattitue : {lat} and longitude : {long}")
            print(f"The past summer temperature at {location} is {temp} degree Celsius")

            print("Now locating it exactly on the map......")

            mapping = folium.Map(location=[lat, long], zoom_start= 30)
            mapping.save("map.html")

            print("Map has been created")
            return
    else:
        print("Location not found!")
        return