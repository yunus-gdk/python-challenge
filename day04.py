# Write a function called only_floats, which takes two
# parameters a and b, and returns 2 if both arguments are floats,
# returns 1 if only one argument is a float, and returns 0 if neither
# argument is a float. If you pass (12.1, 23) as an argument, your
# function should return a 1.


def only_floats(*listArg):
  print(f'{listArg}')
  floatList = []
  for i in listArg:
    if isinstance(i, float): floatList.append(i)
  print(f'Number of float: {len(floatList)}')


only_floats(1, 2.1, 9.999, 3, 4.1, -1.1, 100)
