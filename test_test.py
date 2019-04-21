from opensky_api import OpenSkyApi
count = []
api = OpenSkyApi()
states = api.get_states()
for s in states.states:
    count.append([s.icao24, s.callsign, s.last_contact, s.longitude, s.latitude, s.velocity, s.geo_altitude, s.heading, s.on_ground])
x = ""
for i in count:
    x = x + str(i[3]) + "," + str(i[4]) + "~"
print(x)
