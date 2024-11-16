"""
2. First and Last Letter
Take in one word and output a string formatted like the sample output. Write a function that inputs a word and returns a string formatted as in the sample output. Name this function letterr().

letterr("Hello")  # returns "First letter is H and last letter is o"
letterr("World")  # returns "First letter is W and last letter is d"

"""

#CODE 
#YOUR
#FUNCTION BELOW HERE
def letterr(x):
  return ("First letter is " + (x[0]) + " and last letter is " + (x[len(x)-1]))
x = ""















"""
++++++++++++++++++++
don't code below here
++++++++++++++++++++++
"""
if __name__ == "__main__":
  x = input("Enter in a string: \n")
  print(letterr(x))