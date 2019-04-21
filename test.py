from opensky_api import OpenSkyApi

def test():
    #объект всех самолетов
    api = OpenSkyApi()
    count = []
    # bbox = (min latitude, max latitude, min longitude, max longitude)
    states = api.get_states()
    #присвоение каждому самолету номер
    #для того чтобы в телеграме узнать информацию о нем
    counts = 1
    for s in states.states:
        if "AFL" in s.callsign:
            count.append([s.icao24, s.callsign, s.last_contact, s.longitude, s.latitude, s.velocity, s.geo_altitude, s.heading, s.on_ground, counts, s.origin_country])
            counts += 1
        x = ""
        #формировка запроса для карт (обозначение меток)
        for i in count:
            x = x + str(i[3]) + "," + str(i[4]) + "," + str(i[9]) + "~"   
    return [count, x]
