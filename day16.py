# Write a function called sum_list with one parameter that takes
# a nested list of integers as an argument
# and returns the sum of the integers.
# For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]]
# as an argument your function should return a sum of 33.


def sum_list(nestedValue):
  total = 0
  for listItem in nestedValue:
    for nb in listItem:
      # print(nb)
      total = total + nb
  print(total)


sum_list([[2, 4, 5, 6], [2, 3, 5, 6], [8, 1, 5, 2]])
