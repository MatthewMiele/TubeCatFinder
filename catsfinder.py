import sys
import random
from objects import Cat, Owner, Station
from utils import get_most_visited_stations, get_most_traveled


def generate_lost_cats(num_of_cats):
    cats = []
    owners = []

    stations = Station.import_stations(
        'data/tfl_stations.json', 'data/tfl_connections.json')

    for number in range(num_of_cats):
        cat_station = random.choice(stations)

        owner_stations = list(stations)
        owner_stations.remove(cat_station)
        owner_station = random.choice(owner_stations)

        cat = Cat(number, cat_station)
        owner = Owner(number, cat, owner_station)

        cats.append(cat)
        owners.append(owner)

    return (cats, owners, stations)


def cat_finder(num_of_cats, max_steps):
    cats, owners, stations = generate_lost_cats(num_of_cats)
    all_owners, all_cats = owners[:], cats[:]
    steps_taken_to_find_cat = 0
    step_counter = 0
    trapped_owners = []
    trapped_cats = []
    found_cats = []
    while owners:
        for owner in owners[:]:
            cat = owner.cat
            if cat.station == owner.station:
                owners.remove(owner)
                owner.station.open = False
                found_cats.append(cat)
                steps_taken_to_find_cat += owner.steps
                sys.stdout.write('\r')
                print("{} found {} - {} is now closed.".format(
                        owner, cat, owner.station
                ))
            else:
                owner_steps = owner.move()
                cat_steps = cat.move()
                # If a cat or owner is traped they can never be found.
                # If either have made max_steps number of moves, they are tired
                # and cant move anymore. Both cases they are to be removed
                # from the search
                if owner_steps is None:
                    trapped_owners.append(owner)
                    owners.remove(owner)
                if cat_steps is None:
                    trapped_cats.append(owner)
                    owners.remove(owner)
                if max_steps in (owner_steps, cat_steps):
                    owners.remove(owner)

                if owner_steps is not None:
                    step_counter = owner_steps

        sys.stdout.write('\r')
        sys.stdout.write('{} steps taken of maximum {} steps'.format(
            step_counter, max_steps
        ))

    print("\r############  Finished ############")
    print("Total number of cats: {}".format(num_of_cats))
    print("Number of cats found: {}".format(len(found_cats)))
    print('{} steps taken of maximum {} steps'.format(step_counter, max_steps))
    avg_steps = steps_taken_to_find_cat / len(found_cats) if found_cats else "Infinity"
    print("Average number of movements required to find a cat: {}".format(avg_steps))

    most_visited_stations = get_most_visited_stations(stations)
    most_travled_owners = get_most_traveled(all_owners)
    most_travled_cats = get_most_traveled(all_cats)

    print("Most visited station: {} have {} visits".format(
        most_visited_stations[0], most_visited_stations[1])
    )
    print("Most traveld cat: Cats {} visited {} differnt station".format(
        most_travled_cats[0], most_travled_cats[1])
    )
    print("Most traveld owner: Owners {} visited {} differnt station".format(
        most_travled_owners[0], most_travled_owners[1])
    )
    print("Trapped cats: {}".format(len(trapped_cats)))
    print("Trapped owners: {}".format(len(trapped_owners)))
