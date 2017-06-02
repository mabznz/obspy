# from obspy.core import read
from obspy.clients.fdsn import Client
from obspy.core import UTCDateTime

client = Client("GEONET")

# tr = read("http://service.geonet.org.nz/fdsnws/dataselect/1/query?station=TDHS&location=20&channel=?N?&starttime=2016-09-01T16:37:00.000&endtime=2016-09-01T16:42:00.000")
time = UTCDateTime("2016-09-01T16:37:00.000")

# Get waveforms
# http://docs.obspy.org/packages/autogen/obspy.clients.fdsn.client.Client.get_waveforms.html#obspy.clients.fdsn.client.Client.get_waveforms
# network, station, location, channel, starttime, endtime
tr = client.get_waveforms("NZ", "TDHS", "20", "?N?", time, time + 300)
print(tr)
tr.plot()
