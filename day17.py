# Write a function called user_name,
# that creates a username for the user.
# The function should ask a user to input their name.
# The function should then reverse the name
# and attach a randomly issued number between 0 – 9 at the end of the name.
# The function should return the username.
import random


def user_name():
  newName = []

  name = list(input("What's your name: "))
  for i in name:
    newName.insert(0, i)
  newName.append(str(random.randrange(0, 9)))
  print(newName)
  newNameStr = ''.join(newName)
  print(newNameStr)


user_name()
