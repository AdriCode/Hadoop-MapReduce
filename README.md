# Airline Statistics 👩‍✈️  Final exam - UCPH

The goal of this exercise was to analyze a dataset containing information about flights in the USA from [the Bureau of Transportation Statistics](https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time). 

Each line of the data contains:
- Flight date.
- Airline ID.
- Flight number.
- Origin airport.
- Destination airport.
- Departure time.
- Departure delay (min).
- Arrival time.
- Arrival delay (min).
- Time in air (min).
- Distance between both airports (mi).

## Tasks:

1. **Shortest flight distance:** Mapper & reducer that compute the smallest flight distance per airline ID. The reducer output provides for each line: Airline ID and minimal flight distance.

2. **Late arrival counts:** Mapper & reducer that compute the total number of delayed flights per airline ID. A delayed flight is one with a positive arrival delay. Missing values are treated as 0. The reducer output provides for each line: Airline ID, number of total flights, number of delayed flights and percentage of delayed flights.

3. **Mean and standard deviation for arrival delay:** Mapper & reducer
that compute the mean and standard of the arrival delays for each airline ID, considering the negative ones too. Missing values are treated as 0. It was implemented a combiner to lesser the work of the reducer. The reducer output provides for each line: Airline ID and mean & standard deviation.

4. **Top-10 arrival delays:** Mapper & reducer that compute the 10
most delayed flights for each airline ID, using also a combiner. The reducer output provides for each line: Airline ID and a list of the 10 most delayed flights.

The folder of each task contains the source code files (mapper.py/combiner.py/reducer.py) and the outputs (results.txt) according to the task.

**P.S.:** Answers based on material shared during the course *Large-Scale Data Analysis (LSDA)*.
