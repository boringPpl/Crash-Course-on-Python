'''Question 6.5:
Fill in the blanks to make the factorial function return the factorial of n. 
Then, print the first 10 factorials (from 0 to 9) with the corresponding number. 
Remember that the factorial of a number is defined as the product of an integer 
and all integers before it. 

For example, the factorial of four (4!) is equal to 1*2*3*4=24. 
Also recall that the factorial of zero (0!) is equal to 1.
'''

def factorial(n):
    result = 1
    for x in range(1,___):
        result = ___ * ___
    return ___

for n in range(___,___):
    print(n, factorial(n+___))