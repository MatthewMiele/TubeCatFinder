import random
import json


def get_open_stations(stations):
    return [station for station in stations if station.open]


class Owner():

    def __init__(self, number, cat, station):
        self.number = number
        self.cat = cat
        self.station = station
        station.visited += 1
        self.steps = 0
        self.visited_stations = set()
        self.visited_stations.add(station)

    def move(self):
        open_connections = get_open_stations(self.station.connections)
        if not open_connections:  # Traped! :(
            return None

        choices = list(set(open_connections) - set(self.visited_stations))
        if choices:
            self.station = random.choice(choices)
        else:
            self.station = random.choice(open_connections)

        self.visited_stations.add(self.station)
        self.station.visited += 1
        self.steps += 1
        return self.steps

    def __repr__(self):
        return "Owner {}".format(self.number)


class Cat():

    def __init__(self, number, station):
        self.number = number
        self.station = station
        station.visited += 1
        self.steps = 0
        self.trapped = False
        self.visited_stations = set()

    def move(self):
        open_connections = get_open_stations(self.station.connections)
        if not open_connections:  # Traped! :(
            return None

        self.station = random.choice(open_connections)
        self.visited_stations.add(self.station)
        self.station.visited += 1
        self.steps += 1
        return self.steps

    def __repr__(self):
        return "Cat {}".format(self.number)


class Station():

    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
        self.open = True
        self.connections = set()
        self.visited = 0

    def __repr__(self):
        return self.name

    @classmethod
    def import_stations(cls, stations_file, connections_file):
        stations = []

        with open(stations_file) as stations_data:
            station_data = json.load(stations_data)

        with open(connections_file) as connections_data:
            connections_data = json.load(connections_data)

        for station in station_data:
            sid = station[0]
            name = station[1]
            stations.append(cls(sid, name))

        for connection in connections_data:
            sid = connection[0]  # Station ID
            cid = connection[1]  # Connection ID
            station1 = next(s for s in stations if s.sid == sid)
            station2 = next(s for s in stations if s.sid == cid)
            station1.connections.add(station2)
            station2.connections.add(station1)

        return stations
