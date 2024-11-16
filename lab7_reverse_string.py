"""

7. Reverse String
Write a function reverse_string() that takes a string as a parameter and returns the string reversed.

reverse_string("hello")  # returns "olleh"
reverse_string("world")  # returns "dlrow"
reverse_string("Python")  # returns "nohtyP"

"""

#CODE 
#YOUR
#FUNCTION BELOW HERE


def reverse_string(s):
    return s[::-1]















"""
++++++++++++++++++++
don't code below here
++++++++++++++++++++++
"""
if __name__ == "__main__":
  x = input("Enter in a string to reverse: \n")
  print(reverse_string(x))