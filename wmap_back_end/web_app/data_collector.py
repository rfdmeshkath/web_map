import requests


def dublin_bike_api():
    """
    this function collects dublin bike station data from and api then normalize the data in a dictionary
    :return: list of dictionary
    """
    r = requests.get(
        'https://api.jcdecaux.com/vls/v1/stations?contract=dublin&apiKey=a6c1b6c4bac2222a2b80e49abf91bbfddd45e5e2')
    data = r.json()
    required_data = []
    for item in data:
        temp = {
                'address':   item['address'],
                'available': item['available_bikes'],
                'latitude':  item['position']['lat'],
                'longitude': item['position']['lng']
            }
        required_data.append(temp)
    return required_data

