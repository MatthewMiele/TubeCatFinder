import unittest
from objects import Station


class StationTests(unittest.TestCase):

    def test_create_connections_generates_stations_with_connections(self):
        stations_data = [
            ["1", "Station 1"],
            ["2", "Station 2"],
            ["3", "Station 3"],
            ["4", "Station 4"],
            ["5", "Station 5"]
        ]
        connection_data = [
            ["1", "2"],
            ["3", "5"],
            ["1", "4"],
        ]
        expected_results = {
         "1": ["2", "4"],
         "2": ["1"],
         "3": ["5"],
         "4": ["1"],
         "5": ["3"]
        }

        stations = Station.create_connections(stations_data, connection_data)

        self.assertEqual(len(stations), len(expected_results))

        for station in stations:
            expected_connections = expected_results[station.sid]
            connection_sids = [c.sid for c in station.connections]
            self.assertCountEqual(connection_sids, expected_connections)

    def test_get_open_stations_returns_only_open_station(self):
        open_station_1 = Station("1", "A")
        open_station_2 = Station("2", "B")
        closed_station_1 = Station("3", "C")
        closed_station_1.open = False

        stations = [open_station_1, open_station_2, closed_station_1]
        open_stations = Station.get_open_stations(stations)
        expected_result = [open_station_1, open_station_2]
        self.assertCountEqual(open_stations, expected_result)

    def test_get_open_stations_returns_empty_list_if_none_open(self):
        closed_station_1 = Station("3", "C")
        closed_station_2 = Station("4", "B")
        closed_station_1.open = False
        closed_station_2.open = False

        stations = [closed_station_1, closed_station_2]
        open_stations = Station.get_open_stations(stations)
        expected_result = []
        self.assertCountEqual(open_stations, expected_result)
