from opensky_api import OpenSkyApi

def test():
    api = OpenSkyApi()
    count = []
    # bbox = (min latitude, max latitude, min longitude, max longitude)
    states = api.get_states(icao24=("155be4", "155c0e", "155c0c", "155c0a", "155c16", "155bc1", "155c15", "155be7", "155bd3", "155c0d"))
    for s in states.states:
        count.append([s.icao24, s.callsign, s.last_contact, s.longitude, s.latitude, s.velocity, s.geo_altitude, s.heading, s.on_ground])
        x = ""
        counts = 0
        for i in count:
            counts += 1
            x = x + str(i[3]) + "," + str(i[4]) + "," + str(counts) + "~"   
    return [count, x]
