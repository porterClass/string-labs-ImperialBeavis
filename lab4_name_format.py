"""

4. Name Formatting
Write two functions. last_first() will take in one parameter, a string. This string will be in the format of a name (like "Bugs Bunny"). last_first() will return a new string that is in the "last, first" format "Bunny, Bugs". The second function first_last() will take in a string in the format "last, first" as a parameter. It will return a new string that changes the string back into the original format, "first last".

last_first("James Bond")  # returns "Bond, James"
first_last("Bond, James")  # returns "James Bond"
first_last(last_first("Bugs Bunny"))  # returns "Bugs Bunny"

"""

#CODE 
#YOUR
#FUNCTION BELOW HERE

def last_first(x):
 space = x.find(" ")
 new_string = ""
 last = x[space + 1:]
 first = x[0:space]
 new_string += last + ", " + first


 return new_string


def first_last(y):
 seperate = y.find(", ")
 new_string = ""
 first = y[seperate + 2:]
 last = y[0:seperate]
 new_string += first + " " + last
 return new_string













"""
++++++++++++++++++++
don't code below here
++++++++++++++++++++++
"""
if __name__ == "__main__":
  x = input("Enter your first and last name separated by a space: \n")
  y = input("Enter your last and first name separated by a comma and a space: \n")
  print(last_first(x))
  print(first_last(y))
  print(first_last(last_first(x)))