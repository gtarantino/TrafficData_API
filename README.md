# CSC 436 - Mobile App Dev (iOS)
## Traffic Data Pattern Analyzer - By: Giancarlo Tarantino & Kye Miranda


This project retrieves real-time New York traffic data from the following
[source](http://207.251.86.229/nyc-links-cams/LinkSpeedQuery.txt). We found
this resource [here](https://data.cityofnewyork.us/Transportation/Real-Time-Traffic-Speed-Data/xsat-x5sa)
which is maintained by New York City's Department of Transportation (NYCDOT)
Traffic Management Center (TMC). To learn more about where we found the data,
just follow the previous link.

The data recieved from NYCDOT's TMC is provided in a CSV format. However, we
wanted the data to be structured specifically in JSON. To accomplish this, we
wrote our own script to retrieve, clean, and re-format the data. To run this
script, you need to be in the `scripts` directory and run the fetch traffic
data command.

```
cd TrafficData_API/scripts
./fetchTrafficData
```

After running, you will find the newly created JSON traffic data in the
datasource directory.
```
cd TrafficData_API/datasource
```

We also created a server to host the data locally. If you would like to use this
feature, you need to go to the 'src' directory and run the local server. Here
we used [Flask](http://flask.pocoo.org/) and Python3.

```
cd TrafficData_API/src
python3 server.py
```

Once the server is up and running, hit the following route 'getTrafficData' to
see the traffic data.
