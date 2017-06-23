from obspy.clients.fdsn import Client
import pprint

client = Client('GEONET')
beta = Client(base_url='http://localhost:8080/')

# inventory = client.get_stations(latitude=-41.323457044, longitude=174.805894052, maxradius=0.5, format="xml", level="response")
# bentory = beta.get_stations(latitude=-41.323457044, longitude=174.805894052, maxradius=0.5, format="xml")
# inventory = client.get_stations(minlatitude=-45.0, maxlatitude=-35.0, minlongitude=173, maxlongitude=177, format="xml")

inventory = client.get_stations(station='ARAZ', level='response')
bentory = beta.get_stations(station='ARAZ', level='station')
if inventory == bentory:
    print('equal')
else:
    dic = inventory.get_contents()
    pp = pprint.PrettyPrinter(depth=6)
    pp.pprint(inventory.select('channels'))
# Supported types: STATIONXML, KML, SACPZ, CSS, SHAPEFILE
#inventory.write("inventory.xml", "STATIONXML")
