import requests
import geocoder


def get_my_location():
    """
    gets the location of a user based on ip
    :return: llatitude and longitude of the user
    """
    g = geocoder.ip('me')
    lat = g.latlng[0]
    lng = g.latlng[1]
    return lat, lng


def all_stations():
    """
    connects with the host api and collects information about all the dublin bike stations in Dublin
    :return: formatted list of dictionary which can be directly passed into flask_googlemaps Map object
    """
    response_obj = requests.get(
        'http://51.140.240.121:8080/api/v1/get_all_stations/')
    data = response_obj.json()
    formatted_data = []
    # formatting data for flask_googlemaps
    for i in data.values():
        temp = {
            'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
            'lat': i['latitude'],
            'lng': i['longitude'],
            'infobox': i['address'] + ' | ' + 'Available: ' + str(i['available'])
        }
        formatted_data.append(temp)

    return formatted_data


def station_route_data():
    """
    collects bike stations data which are around 1.5 km radius of the user
    :return:
    """
    # getting current location
    lat, long = get_my_location()
    # receiving bike stations ifo around user location
    response_obj = requests.get(
        'http://51.140.240.121:8080/api/v1/get_stations_near_to_me/?latitude={}&longitude={}'.format(lat, long))
    data = response_obj.json()
    formatted_data = []
    # formatting data
    for i in data.values():
        temp = [str(i['latitude']) + ',' + str(i['longitude']), i['address'] + ' | ' + 'Left ' + str(i['available'])
                + ' | ' + 'Distance ' + str(round(i['distance'], 2)) + 'Km']
        formatted_data.append(temp)
    return formatted_data


def get_nearer_stations(address):
    """
    gets all the bike stations near to a address
    :param address: address of type str
    :return: formatted data for flask_googlemaps
    """
    response_obj = requests.get(
        'http://51.140.240.121:8080/api/v1/get_stations_near_to_a_location/?address={}'.format(address))
    data = response_obj.json()
    formatted_data = []
    for i in data.values():
        temp = {
            'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
            'lat': i['latitude'],
            'lng': i['longitude'],
            'infobox': i['address'] + ' | ' + 'Available: ' + str(i['available'])
        }
        formatted_data.append(temp)

    return formatted_data

