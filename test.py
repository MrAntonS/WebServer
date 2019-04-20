from opensky_api import OpenSkyApi

def test():
    api = OpenSkyApi()
    count = []
    # bbox = (min latitude, max latitude, min longitude, max longitude)
    states = api.get_states()
    counts = 1
    for s in states.states:
        if "AFL" in s.callsign:
            count.append([s.icao24, s.callsign, s.last_contact, s.longitude, s.latitude, s.velocity, s.geo_altitude, s.heading, s.on_ground, counts])
            counts += 1
        x = ""
        for i in count:
            x = x + str(i[3]) + "," + str(i[4]) + "," + str(i[9]) + "~"   
            print(x)
    return [count, x]
