# Write a function called difference
# that takes two lists as arguments.
# This function should return all the elements
# that are in list a but not in list b
# and all the elements in list b not in list a.
# For example:
# list1 = [1, 2, 4, 5, 6]
# list2 = [1, 2, 5, 7, 9]
# should return:
# [4, 6, 7, 9]


def difference(arg1, arg2):
  newArg = []
  for i in arg1:
    if i not in arg2: newArg.append(i)
  for i in arg2:
    if i not in arg1: newArg.append(i)
  print(sorted(newArg))


list1 = [1, 2, 5, 7, 9]
list2 = [1, 2, 4, 5, 6]
difference(list1, list2)
