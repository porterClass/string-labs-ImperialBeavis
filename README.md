[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17031946)
# strings-labs-csp
# CSP Labs to Practice Python Strings

## Strings Labs Unit 5

Write a Python program `string_functions.py` that contains the following functions. **DO NOT USE PYTHON’S REPLACE FUNCTION (METHOD) OR ANY OTHER SHORTCUTS.**

### 1. Concatenate Strings

Write a function `concat()` that takes as parameters two strings and returns the two strings concatenated together. Concatenate means to join two strings together.

```python
concat("hello", "world")  # returns "hello world"
concat("jim", "bob")      # returns "jim bob"
```

### 2. First and Last Letter

Take in one word and output a string formatted like the sample output. Write a function that inputs a word and returns a string formatted as in the sample output. Name this function `letterr()`.

```python
letterr("Hello")  # returns "First letter is H and last letter is o"
letterr("World")  # returns "First letter is W and last letter is d"
```

### 3. Substring

Write a function `substring()` that takes a string and two non-negative integers as parameters and returns a section (substring) of the given string. The first integer is the starting position and the second integer is the position after the last character of the substring.

```python
substring("chicken", 3, 6)  # returns "cke"
substring("alligator", 3, 8)  # returns "igato"
substring("COMPUTER SCIENCE IS THE BEST!", 9, 12)  # returns "SCI"
```

### 4. Name Formatting

Write two functions. `last_first()` will take in one parameter, a string. This string will be in the format of a name (like "Bugs Bunny"). `last_first()` will return a new string that is in the "last, first" format "Bunny, Bugs". The second function `first_last()` will take in a string in the format "last, first" as a parameter. It will return a new string that changes the string back into the original format, "first last".

```python
last_first("James Bond")  # returns "Bond, James"
first_last("Bond, James")  # returns "James Bond"
first_last(last_first("Bugs Bunny"))  # returns "Bugs Bunny"
```

### 5. Replace String

Write a function `replaceString()` that takes an original string, a target string, and a replacement string as parameters and returns a new string with the first instance of the target string replaced with the replacement string.

```python
replaceString("Computer science is fun.", "science", "programming")
# returns "Computer programming is fun."

replaceString("Python is difficult.", "difficult", "really easy")
# returns "Python is really easy."
```
### 6. Count Vowels

Write a function `count_vowels()` that takes a string as a parameter and returns the number of vowels (a, e, i, o, u) in the string.

```python
count_vowels("hello")  # returns 2
count_vowels("world")  # returns 1
count_vowels("Python")  # returns 1
```

### 7. Reverse String

Write a function `reverse_string()` that takes a string as a parameter and returns the string reversed.

```python
reverse_string("hello")  # returns "olleh"
reverse_string("world")  # returns "dlrow"
reverse_string("Python")  # returns "nohtyP"
```

### 8. Count Words

Write a function `count_words()` that takes a string as a parameter and returns the number of words in the string. Words are separated by spaces.

```python
count_words("hello world")  # returns 2
count_words("Python is fun")  # returns 3
count_words("Count the number of words in this sentence.")  # returns 7
```

