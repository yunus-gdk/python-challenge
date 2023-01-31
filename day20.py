# Write a function called capitalize.
# This function takes a string as an argument
# and capitalizes the first letter of each word.
# For example, ‘i like learning’ becomes ‘I Like Learning’.


def capitalize(arg):
  strArg = []
  listArg = arg.split(" ")
  for i in listArg:
    j = i.capitalize()
    strArg.append(j)
  print(' '.join(strArg))


capitalize("i like learning")
