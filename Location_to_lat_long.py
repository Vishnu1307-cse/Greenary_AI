from geopy.geocoders import Nominatim

def get_coordinates(location):
    geoloc = Nominatim(user_agent="geo_locator")
    loc_cord = geoloc.geocode(location)
    if loc_cord:
        return loc_cord.latitude , loc_cord.longitude
    else:
        return None