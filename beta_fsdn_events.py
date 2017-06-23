#! /usr/bin/python3.5
from obspy.clients.fdsn import Client
client = Client(base_url='http://beta-service.geonet.org.nz/')
#client = Client(base_url='http://localhost:8080/')

# events = client.get_events(starttime="2016-11-18T11:00:00.000", endtime="2016-11-20T11:00:00.000", minmagnitude=5, longitude=173.02, latitude=-42.69, maxradius=1, format='csv')
# events = client.get_events(eventid="2016p876450")
# events = client.get_events(starttime="2016-11-20T09:00:00.000", endtime="2016-11-20T11:00:00.000")
# events = client.get_events(starttime="2016-11-20T10:45:00.000", endtime="2016-11-20T11:00:00.000", orderby="time-asc") # magnitide sort order not working, time is
# events = client.get_events(starttime="2016-11-20T10:30:00.000", endtime="2016-11-20T11:00:00.000", longitude=173.02, latitude=-42.69, minradius=0.5, orderby="time-asc")
# events = client.get_events(starttime="2016-11-20T10:30:00.000", endtime="2016-11-20T11:00:00.000", longitude=173.02, latitude=-42.69, maxradius=0.5, orderby="time-asc")

# Not supported
# events = client.get_events(starttime="2016-11-20T10:30:00.000", endtime="2016-11-20T11:00:00.000", longitude=173.02, latitude=-42.69, limit=2, orderby="time-asc")
# events = client.get_events(starttime="2016-11-20T10:30:00.000", endtime="2016-11-20T11:00:00.000", longitude=173.02, latitude=-42.69, offset=2, orderby="time-asc")
# events = client.get_events(starttime="2016-11-20T10:30:00.000", endtime="2016-11-20T11:00:00.000", longitude=173.02, latitude=-42.69, magnitudetype=2, orderby="time-asc")
# events = client.get_events(starttime="2016-11-20T10:30:00.000", endtime="2016-11-20T11:00:00.000", longitude=173.02, latitude=-42.69, includeallorigins=2, orderby="time-asc")
# events = client.get_events(starttime="2016-11-20T10:30:00.000", endtime="2016-11-20T11:00:00.000", longitude=173.02, latitude=-42.69, includeallmagnitudes=2, orderby="time-asc")
events = client.get_events(starttime="2016-11-20T10:30:00.000", endtime="2016-11-20T11:00:00.000", longitude=173.02, latitude=-42.69, includeallarrivals=2, orderby="time-asc")
# print(events)

print(events.__str__(print_all=True))
