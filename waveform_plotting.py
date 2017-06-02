from obspy.core import read

singlechannel = read('https://examples.obspy.org/COP.BHZ.DK.2009.050')
# dt = singlechannel[0].stats.starttime;
# print("Startime:", dt)
# singlechannel.plot(color='red', number_of_ticks=7, tick_rotation=5, tick_format='%I:%M %p', starttime=dt + 60*60, endtime=dt + 60*60 + 120, outfile='singlechannel.png')

# threechannels = read('https://examples.obspy.org/COP.BHE.DK.2009.050')
# threechannels += read('https://examples.obspy.org/COP.BHN.DK.2009.050')
# threechannels += read('https://examples.obspy.org/COP.BHZ.DK.2009.050')
#
# threechannels.plot(size=(800,600))

singlechannel.plot(type='dayplot')
