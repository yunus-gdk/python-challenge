# Write a function called check_pangram that takes a string
# and checks if it is a pangram.
# A pangram is a sentence that contains all the letters of the alphabet.
# If it is a pangram, the function should return True, otherwise, return False.
# The following sentence is a pangram so it should return True:
# 'the quick brown fox jumps over a lazy dog'
import string


def check_pangram(args):
#   print("".join(sorted(set(args.replace(" ", "")))))
#   print(string.ascii_lowercase)

  if "".join(sorted(set(args.replace(" ", "")))) == string.ascii_lowercase:
    print("True")
  else:
    print("False")


test = "the quick brown fox jumps over a lazy dog"
check_pangram(test)
