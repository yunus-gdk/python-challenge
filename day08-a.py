# Write a function called odd_even
# that has one parameter and takes a list of numbers as an argument.
# The function returns the difference between
# the largest even number in the list and the smallest odd number in the list.
# For example,
# if you pass[1,2,4,6] as an argument the function should return 6 - 1 = 5.

listNb = [2, 6, 4, 1]


def odd_even(listNb):
  newList = []
  newList = sorted(listNb, reverse=True)
  result = newList[0] - newList[-1]
  print(f'{result}')


odd_even(listNb)
