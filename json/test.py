from opensky_api import OpenSkyApi
import json


def test(x1, x2, coords1, coords2):
    api = OpenSkyApi()
    count = []
    # bbox = (min latitude, max latitude, min longitude, max longitude)
    states = api.get_states()
    counts = 1
    s = list(filter(lambda x: "AFL" in x.callsign or "SU" in x.callsign, states.states))
    counts += 1
    x = ""
    falg = True
    si = "'["
    for i in s:
        if i.callsign != '' and i.heading != '' and i.icao24 != '' and i.latitude != '' and i.longitude != '' and i.origin_country != '' and i.velocity != '' and falg:
            y = [coords1, coords2]
            si += ' {"OurCoords": ' + '"' +str(y) + '"' + ',' + '"Callsign": ' + '"' + str(i.callsign) + '"' + ',' + '"Heading":' + '"' + str(i.heading) + '"' + ',' + '"icao24":' + '"' + str(i.icao24) + '"' + ',' + '"latitude":' + '"' + str(i.latitude) + '"' + ',' + '"longitude":' + '"' + str(i.longitude) + '"' + ',' + '"Country":' + '"' + str(i.origin_country) + '"' + ',' + '"Velocity":' + '"' + str(i.velocity) + '"' + '},'
        if i.longitude != None and i.latitude != None:
            x = x + str(i.longitude) + "," + str(i.latitude) + "~"   
    si = si[:-1] + "]'"    
    print(si)
    with open('data.json', 'w') as outfile:
        outfile.write("data = " + si)
    #json.dump(str(si), outfile)           
    return [s, x]
test(1,1,1,1)