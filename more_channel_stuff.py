#! /usr/bin/python3.5
import obspy
from obspy.clients.fdsn import Client
# client = Client(base_url='http://beta-service.geonet.org.nz/')
client = Client(base_url='GEONET')

t1 = obspy.UTCDateTime("2016-09-01T16:37:00.000")
t2 = obspy.UTCDateTime("2016-09-01T16:42:00.000")

st = client.get_waveforms('NZ','ARHZ','10','EHE',t1,t2,attach_response=True)
pre_filt = (0.005, 0.006, 30.0, 35.0)
tr = st[0]
# print(tr.stats.response.get_evalresp_response(1.0, 3, 'VEL', 1, 1))
print(tr.stats.response)

inventory = client.get_stations(starttime=t1, endtime=t2, network='NZ', station='ARHZ', location='10', level="response")
print(inventory)
print('Stages from get stations call:', inventory.get_response('NZ.ARHZ.10.EHE', t1))
