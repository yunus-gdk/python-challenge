# Write a function called index_position.
# This function takes a string as a parameter
# and returns the positions or indexes of all lower letters in the string.
# For example, ‘LovE’ should return [1,2]


def index_position(arg):
  indexList = []
  for i in arg:
    if i.islower():
      result = arg.index(i)
      indexList.append(result)
  print(indexList)


index_position("LovE")