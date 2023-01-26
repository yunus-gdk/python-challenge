# Write a function called flat_list
# that takes one argument, a nested list.
# The function converts the nested list into a onedimension list.
# For example [[2,4,5,6]] should return [2,4,5,6].

newValue = []


def flat_list(nestedValue):
  newValue = nestedValue[0]
  print(newValue)


flat_list([[2, 4, 5, 6]])
