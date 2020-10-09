'''Question 5.2:
Complete the function digit(x) that returns how many digits the number has. 
For example: 7 has 1 digit, 47 has 2 digits, and 355 has 3 digits. 

Tip: you can figure out the digits of a number by dividing it by 10 once per digit 
until there are no digits left.
'''

def digit(x):
	count = 0
	if x == 0:
	  ___
	while (___):
		count += 1
		___
	return count
	
print(digit(7))   # Should print 1
print(digit(47))  # Should print 2
print(digit(355)) # Should print 3
print(digit(1200))    # Should print 4