#! /usr/bin/python3.5
from obspy.clients.fdsn import client
client = Client(base_url='http://beta-service.geonet.org.nz/')
#client = Client(base_url='http://localhost:8080/')

inventory = client.get_stations(starttime="2016-11-13 11:00:00.000", endtime="2016-11-20 11:00:00.000", level="response", station="ARAZ")

print(inventory)
# # Supported types: STATIONXML, KML, SACPZ, CSS, SHAPEFILE
# inventory.write("inventory.xml", "STATIONXML")
