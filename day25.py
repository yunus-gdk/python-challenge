# Write a function called read_backwards
# that takes a string as an argument and reverses it.
# str1 = "the love is real"
# For example, the string above should return: "real is love the"


def read_backwards(arg):
  listArg = []
  listArg = arg.split(" ")
  listArg.reverse()
  newArg = " ".join(listArg)
  print(newArg)


read_backwards("the love is real")