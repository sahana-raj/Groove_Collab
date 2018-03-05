Required packages-
  geocoder 1.8.0
  zipcode 2.0.0
Python version- 3.6.3
Reference-
  Calculate distance between two geo-codes
  StackoverFlow (using Haversine formula)
  https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula/21623206#21623206

Assumptions-
1.) The zip code input is a valid 5 digit zipcode
2.) The address input is a non empty String
3.) The output for both the text and json formats contains the store name, street address, city, state, zip code  and the distance in km/mi
To run the program, run the following commands-
1.) pip install geocoder
2.) pip install zip_code
3.) python storeFinder.py find_store --zip=93063 --output=json

Notes-
The solution is built on the possibility that a given input ,which is a valid address/zip code in State 'A' might be closer to a store in State 'B' rather than a store in State 'A'.
Since the problem did not specifically mention this case/possibility I will be calculating the distance from the geo code of the input address or the zip code with all records in the given data set.
Filtering the data set based on the state/city would speed up the solution due to less number of records being processed with each input.

Tests-
The 10 test cases in the tests.py file cover all the conditions around different arguments in the commands.
To run the tests-
python tests.py
