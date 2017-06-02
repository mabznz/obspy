from obspy import read

st = read('http://examples.obspy.org/RJOB_061005_072159.ehz.new')
print(st)
print("Length of file:", len(st))
tr = st[0]
print("Length of waveform data:", len(tr.data))
print("Waveform data:", tr.data)
print("First five plots of waveform data:", tr.data[0:5])
st.plot()
