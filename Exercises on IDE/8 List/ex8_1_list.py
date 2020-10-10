'''Question 8.1:
A teacher with two assistants, Amy and Danny, wants an attendance list of the students, 
in the order that they arrived in the classroom. Danny was the first one to note which students arrived, 
and then Amy took over. 

After the class, they each entered their lists into the computer and emailed them to the teacher, 
who needs to combine them into one, in the order of each student's arrival. 
Amy emailed a follow-up, saying that her list is in reverse order. 

Complete the steps to combine them into one list as follows: 
the contents of Danny's list, followed by Amy's list in reverse order, 
to get an accurate list of the students as they arrived.
'''

def combine_list(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  
	
Amy_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Danny_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_list(Amy_list, Danny_list))
