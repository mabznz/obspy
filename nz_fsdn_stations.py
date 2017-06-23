#! /usr/bin/python3.5
from obspy.clients.fdsn import Client as Client

client = Client('GEONET')

inventory = client.get_stations(network="NZ", station='ARAZ', level="response")
# events = client.get_events(starttime="2016-11-13 11:00:00.000", endtime="2016-11-20 11:00:00.000", minmagnitude=5, longtitude=173.02, latitude=-42.69, maxradius=1.0, minradius=1.0)

print(inventory)
#
inventory.write("inventory.xml", "STATIONXML")
