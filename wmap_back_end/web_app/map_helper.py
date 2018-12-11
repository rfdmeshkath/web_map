import json
import requests
import pyproj
from shapely import geometry


def distance_checker(lat, lon, check_lat, check_lon):
    """
    this function checks the distance between two map points
    :param lat: point A's latitude
    :param lon: point A's longitude
    :param check_lat: point B's latitude
    :param check_lon: point B's longitude
    :return: distance in between two points in kilometers
    """
    # ESPG:4326(WGS84) - Initiate coords system for GeoJSON
    crs_wgs = pyproj.Proj(init='epsg:4326')
    # ESPG:27700(OSGB 1936) Initialise British National Grid as it covers Ireland aswell
    crs_bng = pyproj.Proj(init='epsg:27700')
    # convert the points to XY coordinates
    x1, y1 = pyproj.transform(crs_wgs, crs_bng, lon, lat)
    # covert second point to XY coords
    x2, y2 = pyproj.transform(crs_wgs, crs_bng, check_lon, check_lat)
    # create point one and two using x1 y1 and x2 y2
    point_1 = geometry.Point(x1, y1)
    point_2 = geometry.Point(x2, y2)
    # return the distance between the two points
    distance = point_1.distance(point_2) / 1000
    return distance


def retrieve_coordinates_from_address(address):
    """
    this function retrives coordinates from a given address.
    to do this i am using google map api
    :param address: string
    :return: latitude and longitude of the given address
    """
    google_api_key = "AIzaSyB4o2cd-u-d8BCIhTMtHerz9o5S_uxeme4"  # my api key from google
    address = address + " dublin ireland"  # appending dublin ireland to narrow down the search scope
    api_query_url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(address,
                                                                                                 google_api_key)
    google_reply = requests.get(api_query_url)
    location_data = json.loads(google_reply.text)
    latitude = location_data['results'][0]['geometry']['location']['lat']
    longitude = location_data['results'][0]['geometry']['location']['lng']
    return latitude, longitude
