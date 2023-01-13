# Create a function called biggest_odd
# that takes a string of numbers
# and returns the biggest odd number in the list.
# For example, if you pass ‘23569’ as an argument,
# your function should return 9.
# Use list comprehension.

stringNumber = "21594"
listNumber = []


def biggest_odd(stringNumber):
  i = 0
  while i < len(stringNumber):
    listNumber.append(int(stringNumber[i]))
    i += 1
  newList = []
  newList = sorted(listNumber, reverse=True)

  print(newList[0])


biggest_odd(stringNumber)
