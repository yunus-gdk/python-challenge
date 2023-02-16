# Write a function called multiply_words that takes a string as an
# argument and multiplies the length of each word in the string by
# the length of other words in the string.
# For example, the string above should return 240 - love (4) live (4) and (3) laugh (5).
# However, your function should only multiply words will all lowercase letters.
# If a word has one upper case letter, it should be ignored.
# For example, the following string:
# s = "Hate war love Peace" should return 12 – war (3) love (4).
# Hate and Peace will be ignored because they have at least one uppercase letter.
import re


def multiply_words(arg):
  strArg = []
  res = 1
  for i in arg.split(" "):
    if not bool(re.match(r'\w*[A-Z]\w*', i)):
      strArg.append(i)
  for i in strArg:
    res *= len(i)
  print(res)


multiply_words("Hate war love Peace")
