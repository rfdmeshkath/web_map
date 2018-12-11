let dataSet = [];
    $.ajax({
        method: 'GET',
        url: proxyurl + "http://139.59.186.106/json_all_stations/",
        data:{'lat':position.coords.latitude,'long':position.coords.longitude},
        success: function (bike_data) {
        alert('Stations have been loaded');
            for (i in bike_data['0']) {
            let row = [];
                            a = bike_data;
                            //Find coords of bike station

                            coords = a['0'][i]['fields']['position'];

                            //Regex for seperating lat and lng into a variable

                            let regExp = /\(([^)]+)\)/;
                            let matches = regExp.exec(coords);

                            //matches[1] contains the value between the parentheses

                            splitting = matches[1].split(" ");
                            lng = splitting[0];
                            lat = splitting[1];

                            //Pushing data to a list for displaying later

                            row.push(a['0'][i]['pk']);
                            row.push(a['0'][i]['fields']['stand_name']);
                            row.push(a['0'][i]['distance']);
                            row.push(a['0'][i]['fields']['available_bikes']);

                            //Pushing all bike data station details to the datatables view

                            dataSet.push(row);
            //create the marker for the bike station
            L.marker([lat,lng]).addTo(map).bindPopup("<hr><b>Number: </b>"+ a['0'][i]['pk'] +"<br><b>Name: </b>" + a['0'][i]['fields']['stand_name'] +
                "<br><b>Free bikes: </b> " + a['0'][i]['fields']['available_bikes'] + "<hr><b>Total stands: </b>" + a['0'][i]['fields']['total_bike_stands'] +
                "<hr><b>Free stands: </b> " + a['0'][i]['fields']['available_bike_stands'] + "<hr><b>Updated: </b>" + a['0'][i]['fields']['last_update'] +
                "<hr><b>Position: </b>" + lat + lng + "<hr>"+
                 "<hr><b>Distance: </b>" +a['0'][i]['distance'] +"<hr>"
                +"<br><button class='btn btn-primary' onclick=\"route_to_station(" + position.coords.latitude + "," + position.coords.longitude + "," + lat + "," + lng +")\">Route to here</button>");
            }


            if (x !== '') {
                L.Routing.control({
                        waypoints: [L.latLng(users_lat_coords, users_lng_coords), L.latLng(x, y)],
                        lineOptions: {addWaypoints: false}
                    }
                ).addTo(map);
            }

                        //Data table displaying to the user
                        //
                        $('#example').DataTable({
                            data: dataSet,
                            columns: [
                                {title: "#"},
                                {title: "Name"},
                                {title: "Distance (Km)"},
                                {title: "Free Bikes"}

                            ],

                        });

        },


        error(){alert("No Stations available")}
    });
