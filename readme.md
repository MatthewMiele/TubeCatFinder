```
 _____       _            _____         _   ______  _             _                           _,'|             _.-''``-...___..--';)
|_   _|     | |          /  __ \       | |  |  ___|(_)           | |                         /_ \'.      __..-' ,      ,--...--'''
  | | _   _ | |__    ___ | /  \/  __ _ | |_ | |_    _  _ __    __| |  ___  _ __             <\    .`--'''       `     /'
  | || | | || '_ \  / _ \| |     / _` || __||  _|  | || '_ \  / _` | / _ \| '__|             `-';'               ;   ; ;
  | || |_| || |_) ||  __/| \__/\| (_| || |_ | |    | || | | || (_| ||  __/| |          __...--''     ___...--_..'  .;.'
  \_/ \__,_||_.__/  \___| \____/ \__,_| \__|\_|    |_||_| |_| \__,_| \___||_|         (,__....----'''       (,..--'' 
```

TubeCatFinder is there to help owners and lost cats, who are stuck on the London Underground, reunite.
Each cat and owner take 1 move each per round until they are reunited. Once reunited the station they are at must close and once closed cannot be reentered. If a cat or owner is trapped (stations either side of them are closed and so cant move) they are remove from the search as they will never be found. If a cat or owner has taken 100,000 steps then they are very tired and dont have the energy to keep searching, so they are also removed.

The full details can be found at task-description.txt

## Usage ##
```
python main.py NUMOFCATS --max_steps

NUMOFCATS    How many inital cats and owners are lost :( 
--max_steps  Change how many steps before they get too tired and stop searching (Default: 100,000)
```

## Tests ##
To run the tests simply run
```
python -m unittest tests
```