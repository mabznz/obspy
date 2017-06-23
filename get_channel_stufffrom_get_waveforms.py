#! /usr/bin/python3.5
import obspy
from obspy.clients.fdsn import Client
# client = Client(base_url='http://beta-service.geonet.org.nz/')
client = Client(base_url='GEONET')

t1 = obspy.UTCDateTime("2016-09-01T16:37:00.000")
t2 = obspy.UTCDateTime("2016-09-01T16:42:00.000")

st = client.get_waveforms('NZ','TDHS','20','BN1',t1,t2,attach_response=True)
tr = st[0]
print(tr.stats.response.get_sacpz())
