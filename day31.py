# Write a function that has one parameter and takes a list of words as an argument.
# The function returns the longest word from the list.
# Name the function longest_word.
# The function should return the longest word and the number of letters in that word.
# For example, if you pass [‘Java, ‘JavaScript’, ‘Python’],
# your function should return [10, JavaScript] as the longest word.


def longest_word(args):
  wordLen = []
  for i in args:
    wordLen.append(len(i))
  print(wordLen)

  max_value = max(wordLen)
  max_index = wordLen.index(max_value)

  itemToSearch = [
    item for (index, item) in enumerate(wordLen) if index == max_index
  ]
  word = [item for (index, item) in enumerate(args) if index == max_index]
  print(itemToSearch + word)


longest_word(["Java", "JavaScript", "Python"])
