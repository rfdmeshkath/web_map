from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

from api_helper import all_stations, station_route_data, get_nearer_stations

app = Flask(__name__)
# my google map api key
app.config['GOOGLEMAPS_KEY'] = "AIzaSyB4o2cd-u-d8BCIhTMtHerz9o5S_uxeme4"
GoogleMaps(app)


@app.route("/show_all_stations")
def show_all_stations():
    """
    this view will show the all the stations available in Dublin
    :return: HTML template
    """
    markers = all_stations()
    db_map = Map(
        identifier="db_map",
        lat=53.234,
        lng=-6.239999,
        markers=markers,
        fit_markers_to_bounds=True
    )
    db_map.style = 'height:95vh;width:98.5vw;margin:0;'
    return render_template('stations.html', db_map=db_map)


@app.route("/routes_to_nearer_stations")
def search_stations():
    """
    this view will show routes to all near dublin bike station to user
    :return: HTML template
    """
    results = station_route_data()
    return render_template('routes.html', results=results)


@app.route("/nearer_station_to_a_address", methods=['GET', 'POST'])
def nearer_stations():
    """
    this view will show all the nearer bike station of a given address
    :return: HTML template
    """
    if request.method == 'GET':
        return render_template('search.html', sl_map='')

    elif request.method == 'POST':
        address = request.form.get('searched_address')
        markers = get_nearer_stations(address)
        sl_map = Map(
            identifier="db_map",
            lat=53.234,
            lng=-6.239999,
            markers=markers,
            fit_markers_to_bounds=True
        )
        sl_map.style = 'height:95vh;width:98.5vw;margin:0;'
        return render_template('search.html', sl_map=sl_map)


if __name__ == "__main__":
    app.run(debug=True)
