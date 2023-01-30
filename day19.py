# Write two functions.
# The first function is called count_words which takes a string of words
# and counts how many words are in the string.

# The second function called count_elements takes a string of words
# and counts how many elements are in the string.
# Do not count the whitespaces.

# The first function will return the number of words in a string
# and the second one will return the number of elements (less whitespace).
# If you pass ‘I love learning’, the count_words function should return
# 3 words and count_elements should return 13 elements.

strArg = input("Enter a string: ")


def count_words(strArg):
  newList = list(strArg.split(" "))
  print(len(newList))
  return newList


def count_elements(newList):
  total = 0
  newList = list(strArg.split(" "))
  for i in newList:
    total += len(i)
  print(total)


count_words(strArg)
count_elements(strArg)
