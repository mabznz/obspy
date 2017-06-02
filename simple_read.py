#!/usr/bin/python

# http://docs.obspy.org/tutorial/code_snippets/python_introduction.html

import glob
from obspy.core import read

for file in glob.glob('*.mseed'):
    print ("File: ", file)
    st = read(file) # Cool. Recognises the differnet file types.
    tr = st[0]
    print ("Station %s Starttime %s Mean data %f Std data %f" % (tr.stats.station, str(tr.stats.starttime), tr.data.mean(), tr.data.std()))
