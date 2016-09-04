def get_most_visited_stations(stations):
    visits = [[s.visited, s.name] for s in stations]
    visits.sort(reverse=True)
    biggest_visit = visits[0][0]
    return [
        [obj[1] for obj in visits if obj[0] == biggest_visit],
        biggest_visit
    ]


def get_most_traveled(objects):
    """ Finds who has visited the most stations """
    visits = [[len(o.visited_stations), o.number] for o in objects]
    visits.sort(reverse=True)
    most_traveled = visits[0][0]
    return [
        [obj[1] for obj in visits if obj[0] == most_traveled],
        most_traveled
    ]
