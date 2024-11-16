"""
1. Concatenate Strings
Write a function concat() that takes as parameters two strings and returns the two strings concatenated together. Concatenate means to join two strings together.

concat("hello", "world")  # returns "hello world"
concat("jim", "bob")      # returns "jim bob"

"""

#CODE 
#YOUR
#FUNCTION BELOW HERE


def concat(a, b):
  return (a + " " + b)











"""
++++++++++++++++++++
don't code below here
++++++++++++++++++++++
"""
if __name__ == "__main__":
  x = input("Enter in a string: \n")
  y = input("Enter in another string: \n")
  print(concat(x,y))