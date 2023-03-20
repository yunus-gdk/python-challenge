# Write a function called repeated_name
# that finds the most repeated name in the following list.
# name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]


def repeated_name(args):
  unique_list = []
  nbElement = []

  for i in args:
    if i not in unique_list:
      unique_list.append(i)

  for i in unique_list:
    element = 0
    for j in args:
      if i == j:
        element += 1
    nbElement.append(element)

  max_value = max(nbElement)
  max_index = nbElement.index(max_value)

  itemToSearch = [
    item for (index, item) in enumerate(unique_list) if index == max_index
  ]
  print(itemToSearch)


repeated_name([
  "John", "Peter", "John", "Peter", "Jones", "Peter", "Jones", "Jones", "Jones"
])
