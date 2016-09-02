One of the topics streetlife users talk about is missing cats. Cats run away
from their houses all the time and that's really inconvenient for their owners.

Because we care about cats - cats are cute! We are thinking about releasing a
new feature which will allow owners to find their cats... but we need to first
determine how likely is that an owner will find their cat. Streets are dangerous
at night!

In order to do an estimation, we have created a prototype map of London using
it's tube stations. The plan is to run a simulation placing random owners and
cats all around the tube map and check how long it takes them to find each other.

We provide you with the map in the following format:

tfl_stations.csv: station_id, station_name.
tfl_connections.csv: station_id_1, station_id_2.
tfl_stations.json: same as tfl_stations.csv but in JSON format.
tfl_connections.json: same as tfl_connections.csv but in JSON format.

- You should create N owners and N cats, where N is specified as a command-line.
- The initial position of the owner and the cat must be random and different one to the other.
- Any number of owners and cats can start in the same station.
- Because cats are not very intelligent, on each turn they'll travel randomly to one of the stations
  connected to where they are.
- Humans are more intelligent, they will travel to one of the stations connected to where they are,
  but (if possible) not using a station they use before.

Every time an owner finds their cat the amount of love released is THAT big
that TFL needs to close the station to clean the love from the walls.

When a station is closed, owners and cats can leave it using any available route,
but nobody can visit this station again.

It is possible that owners and cats can get "trapped" in a station because there is
no available route to leave the stations -- that's ok, we don't care - that's life.

You should create a program that reads in the tube map, creates N
owners and cats, and unleashes them. The program should run until all the
owners have found their cats, or each owner and cat has moved 100,000 times.

When an owner finds their cat the output should be:

Owner 14 found cat 14 - Picadilly Circus is now closed.

Once the program has finished, it should print out:

Total number of cats: 200
Number of cats found: 25
Average number of movements required to find a cat: 34

If you want to calculate any other metric like for example the most visited station
or the owner with less luck... feel free to include them in the final output.

Review notes:
 - We are not looking for speed, we are looking for a readable elegant solution.
 - It is ok to make assumptions as far as you write them in a comment.
 - Feel free to write tests (If you wish)
