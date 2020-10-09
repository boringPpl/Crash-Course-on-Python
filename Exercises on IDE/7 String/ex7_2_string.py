'''Question 7.2:
Using the format method, fill in the gaps in the convert_distance function 
so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. 

For example, convert_distance(12) should return "12 miles equals 19.2 km".
'''

def convert_distance(km):
	miles = km * 0.621  # 1km is equal to approximately 0.621 miles
	result = "{} km equals {} miles"
	return result

print(convert_distance(19.2)) # Should be: 19.2 km equals 11.92 miles
print(convert_distance(8.8)) # Should be: 8.8 km equals 5.46 miles
print(convert_distance(17.6)) # Should be: 17.6 km equals 10.92 miles


