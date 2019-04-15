from opensky_api import OpenSkyApi

def test():
    api = OpenSkyApi()
    count = []
    # bbox = (min latitude, max latitude, min longitude, max longitude)
    states = api.get_states()
    for s in states.states:
        if s.callsign[0:3] == "AFL" or s.callsign[0:2] == "SU":
            count.append([s.icao24, s.callsign, s.last_contact, s.longitude, s.latitude, s.velocity, s.geo_altitude, s.heading, s.on_ground])
    return count


