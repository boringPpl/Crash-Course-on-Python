'''Question 8.4:
Let's create a function that turns text into pig latin: 
a simple text transformation that modifies each word 
moving the first character to the end, and appending "ay" to the end. 

For example, python ends up as ythonpay.
'''
def pig_latin(text):
  say = ""
  # Separate the text into words
  sentence = ___
  for word in sentence:
    # Create the pig latin word and add it to the list
    ___
    # Turn the list back into a phrase
  return ___
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"