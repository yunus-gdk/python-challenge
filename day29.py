# Write a function called middle_figure
# that takes two parameters a, and b. The two parameters are strings.
# The function joins the two strings and finds the middle element.
# If the combined string has a middle element,
# the function should return the element, otherwise, return ‘no middle figure’.
# Use ‘make love’ as an argument for a and ‘not wars’ as an argument for b.
# Your function should return ‘e’ as the middle element.
# Whitespaces should be removed


def middle_figure(a, b):
  a = a.replace(" ", "")
  b = b.replace(" ", "")
  c = a + b
  if (len(c) % 2) == 1:
    indexMiddle = int(len(c) / 2)
    print(c[indexMiddle])
  else:
    print("no middle figure")


middle_figure("make love", "not wars")
