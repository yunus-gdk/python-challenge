# Write a function called convert_add that takes a list of strings
# as an argument and converts it to integers and sums the list. For
# example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
# summed to 9.

def convert_add():
  mylist = ["1", "3", "5"]
  mylistint = []
  total = 0
  for i in mylist:
    i = int(i)
    total += i
    mylistint.append(i)
  print(mylistint)
  print(total)