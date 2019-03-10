from opensky_api import OpenSkyApi
import sqlite3


api = OpenSkyApi()
count = []
# bbox = (min latitude, max latitude, min longitude, max longitude)
states = api.get_states()
for s in states.states:
    if s.callsign[0:3] == "AFL" or s.callsign[0:2] == "SU":
        count.append([s.icao24, s.callsign, s.last_contact, s.longitude, s.latitude, s.velocity, s.geo_altitude, s.heading, s.on_ground])
print(count)


class DB:
    def __init__(self):
        conn = sqlite3.connect('planes.db', check_same_thread=False)
        self.conn = conn

    def get_connection(self):
        return self.conn

    def __del__(self):
        self.conn.close()


class Planes():
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS planes
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             icao24 VARCHAR(50),
                             callsign VARCHAR(128),
                             last_contact VARCHAR(128),
                             longitude VARCHAR(128),
                             latitude VARCHAR(128),
                             velocity VARCHAR(128),
                             geo_altitude VARCHAR(128),
                             heading VARCHAR(128),
                             on_ground VARCHAR(128)
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, icao24, callsign, last_contact, longitude, latitude, velocity, geo_altitude, heading, on_ground):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users 
                          (icao24, callsign, last_contact, longitude, latitude, velocity, geo_altitude, heading , on_ground) 
                          VALUES (?,?,?,?,?,?,?,?,?)''', (icao24, callsign, last_contact, longitude, latitude, velocity, geo_altitude, heading, on_ground))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM planes WHERE id = ?", (str(user_id),))
        row = cursor.fetchone()
        return row

Planes(DB().get_connection()).insert(count[0],count[1],count[2],count[3],count[4],count[5],count[6],count[7],count[8])