'''Question 8.5:
The guest_list function reads in a list of tuples with the name, age, 
and profession of each party guest, and prints the sentence 
"Guest is X years old and works as __." for each one. 

For example, guest_list(('John', 45, "Chef"), ("Luna", 28, 'Lawyer'), ('Amy', 25, "Engineer")) 
should print out: 
John is 45 years old and works as Chef. 
Luna is 35 years old and works as Lawyer. 
Amy is 25 years old and works as Engineer. 

Fill in the gaps in this function to do that.
'''
def guest_list(guests):
	for ___:
		___
		print(___.format(___))

guest_list([('John', 45, "Chef"), ("Luna", 28, 'Lawyer'), ('Amy', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
John is 45 years old and works as Chef
Luna is 28 years old and works as Lawyer
Amy is 25 years old and works as Engineer
"""

