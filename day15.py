# Write a function called same_in_reverse that takes a string
# and checks if the string reads the same in reverse.
# If it is the same, the code should return True
# if not, it should return False.
# For example, ‘dad’ should return True,
# because it reads the same in reverse.


def same_in_reverse(strTested):
  listStrAppended = []
  listStr = list(strTested)
  for i in listStr:
    listStrAppended.insert(0, i)
  newStr = ''.join(listStrAppended)

  if strTested == newStr: print(True)
  else: print(False)


same_in_reverse("dadoodad")
