"""
3. Substring
Write a function substring() that takes a string and two non-negative integers as parameters and returns a section (substring) of the given string. The first integer is the starting position and the second integer is the position after the last character of the substring.

substring("chicken", 3, 6)  # returns "cke"
substring("alligator", 3, 8)  # returns "igato"
substring("COMPUTER SCIENCE IS THE BEST!", 9, 12)  # returns "SCI"

"""
#CODE 
#YOUR
#FUNCTION BELOW HERE
def substring(s, start, end):
    return s[start:end]














"""
++++++++++++++++++++
don't code below here
++++++++++++++++++++++
"""
if __name__ == "__main__":
  x = input("Enter in a string: \n")
  y = int(input("Enter in a starting position: \n"))
  z = int(input("Enter in a ending position: \n"))
  print(substring(x,y,z))