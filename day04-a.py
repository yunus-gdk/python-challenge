# Write a function called word_index that takes one argument,
# a list of strings and returns the index of the longest word in the
# list. If there is no longest word (if all the strings are of the same
# length), the function should return zero (0).
# For example, the list below should return 2.
# words1 = ["Hate", "remorse", "vengeance"]
# And this list below, shoul return zero (0)
# words2 = ["Love", "Hate"]


def word_index(*listArg):
  # print(f'{listArg}')
  nbLetterList = []
  newList = []

  for i in listArg:
    nbLetterList.append(str(len(i)))
    for j in nbLetterList:
      if j not in newList: newList.append(j)

  print(nbLetterList)
  print(newList)

  # there is 1 longest word
  if len(nbLetterList) == len(newList):
    print("2")
    # there is no longest word
  else:
    print("0")


word_index("Hate", "remorse", "vengeance")
