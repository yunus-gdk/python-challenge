# Write a function called longest_value that takes a dictionary
# as an argument and returns the first longest value of the
# dictionary. For example, the following dictionary should return
# – apple as the longest value.
# fruits = {'fruit': 'apple', 'color': 'green'}


def longest_value():
  dic = {'fruit': 'apple', 'country': 'france', 'color': 'green'}
  longest_value = 0
  # return list(dic.values())
  for value in dic.values():
    # print(value, ":", len(value))
    if len(value) > longest_value:
      longest_value = len(value)
      longest_value_item = value
  print(longest_value_item, ":", longest_value, "caracters")
