'''Question 4.3:
Students in a class receive their grades as Pass/Fail. 
Scores of 50 or more (out of 100) mean that the grade is "Pass". 
For lower scores, the grade is "Fail". 
In addition, scores above 90 (not included) are graded as "Top Score". 
Fill in this function so that it returns the proper grade.
'''

def exam_grade(score):
	if ___:
		grade = "Top Score"
	elif ___:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(45)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(90)) # Should be Pass
print(exam_grade(91)) # Should be Top Score
print(exam_grade(0)) # Should be Fail