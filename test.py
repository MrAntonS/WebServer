from opensky_api import OpenSkyApi
import json


def test(x1, x2, coords1, coords2):
    #объект всех самолетов
    api = OpenSkyApi()
    count = []
    # bbox = (min latitude, max latitude, min longitude, max longitude)
    states = api.get_states()
    #присвоение каждому самолету номер
    #для того чтобы в телеграме узнать информацию о нем
    counts = 1
    s = list(filter(lambda x: x.longitude != None and x.longitude >= x1 and x.longitude <= x2, states.states))
    s = s[:500:5]
    #s = states.states[0:1000]
    counts += 1
    x = ""
    #формировка запроса для карт (обозначение меток)
    falg = True
    si = []
    for i in s:
        with open('data.json', 'w') as outfile:
            if i.callsign != '' and i.heading != '' and i.icao24 != '' and i.latitude != '' and i.longitude != '' and i.origin_country != '' and i.velocity != '':
                si.append({'OurCoords': [coords1, coords2],'Callsign': i.callsign, 'Heading': i.heading, 'icao24': i.icao24, 'latitude': i.latitude, 'longitude': i.longitude, 'Country': i.origin_country, 'Velocity': i.velocity})
                json.dump(si, outfile)           
                falg = False
        if i.longitude != None and i.latitude != None:
            x = x + str(i.longitude) + "," + str(i.latitude) + "~"   
    return [s, x]