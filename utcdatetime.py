#!/usr/bin/python
from obspy.core import UTCDateTime

x = UTCDateTime("2012-09-07T12:15:00")

print(x)

y = UTCDateTime("2012-09-07T12:15:00+02:00")

print(y)

time = UTCDateTime("2012-09-07T12:15:00+02:00")

print ("Year %i" % (time.year))
print ("Julian day %i" % (time.julday))
print ("Timestamp %f" % (time.timestamp))
print ("weekday %f" % (time.weekday))
