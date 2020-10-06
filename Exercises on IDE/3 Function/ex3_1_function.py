''' Question 3.1:
This function converts kilometers (km) to miles.
1. Complete the function. Your function receive the input kilometers, and return the value miles
2. Call the function to convert the trip distance from kilometers to miles
3. Fill in the blank to print the result of the conversion
4. Calculate the round-trip in miles by doubling the result, and fill in the blank to print the result
'''

# 1) Complete the function to return the result of the conversion
def convert_distance(km):
	miles = km * 0.621  # 1km is equal to approximately 0.621 miles

trip_in_km = 50

# 2) Convert trip_in_km to miles by calling the function above
trip_in_miles = ___

# 3) Fill in the blank to print the result of the conversion
print("The distance in miles is " + ___)

# 4) Calculate the round-trip in miles by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in miles is " + ___)
