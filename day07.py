# Write a function called string_range that takes a singlenumber
# and returns a string of its range.
# The string characters should be separated by dots(.)
# For example, if you pass 6 as an argument,
# your function should return ‘0.1.2.3.4.5’.


def string_range(nb):
  i = 0
  j = k = lastStr = ""
  while i < nb:
    j = str(i)
    k = k + j + "."
    i += 1
  lastStr = k.rstrip(k[-1])
  print(lastStr)


string_range(6)
