'''Question 6.3:
The display_even function returns a space-separated string 
of all positive numbers that are divisible by 2, up to and 
including the maximum number that's passed into the function. 

For example, display_even(4) returns “2 4”. Fill in the blank to make this work.
'''

def display_even(max_num):
	return_string = ""
	for x in ___:
		return_string += str(x) + " "
	return return_string.strip()

print(display_even(6))  # Should be 2 4 6
print(display_even(10)) # Should be 2 4 6 8 10
print(display_even(1))  # No numbers displayed
print(display_even(3))  # Should be 2
print(display_even(0))  # No numbers displayed