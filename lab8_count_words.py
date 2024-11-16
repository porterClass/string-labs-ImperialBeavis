"""
8. Count Words
Write a function count_words() that takes a string as a parameter and returns the number of words in the string. Words are separated by spaces.

count_words("hello world")  # returns 2
count_words("Python is fun")  # returns 3
count_words("Count the number of words in this sentence.")  # returns 7

"""

#CODE 
#YOUR
#FUNCTION BELOW HERE

def count_words(input_string):
    return len(input_string.split())
















"""
++++++++++++++++++++
don't code below here
++++++++++++++++++++++
"""
if __name__ == "__main__":
  x = input("Enter in a sentence to count the words of: \n")
  print(count_words(x))