from obspy import read

st = read('http://examples.obspy.org/RJOB_061005_072159.ehz.new')
print(st)
print ("Length:", len(st))
tr = st[0]
print(tr)
print("Seismogram meta data\n", tr.stats)
print("gse2 instrument\n", tr.stats.gse2)
print("gse2 instrument datatype\n", tr.stats.gse2.datatype)
