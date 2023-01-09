# You are given a list of names, and you are asked to write a code that
# returns all the names that start with ‘S’.
# Your code should return a dictionary of all the names that start with S
# and how many times they appear in the dictionary.
# Here is a list below:
# names = ["Joseph","Nathan", "Sasha", "Kelly","Muhammad", "Jabulani", "Sera”, "Patel", "Sera”]
# Your code should return: {“Sasha”: 1, “Sera”: 2}


def return_list():
  names = [
    "Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera",
    "Patel", "Sera"
  ]
  newList = []
  nbItem = {}
  for name in names:
    if name[0] == "S": newList.append(name)
  for i in newList:
    if not i in nbItem:
      nbItem[i] = 1
    else:
      nbItem[i] +=1
  print(nbItem)

return_list()