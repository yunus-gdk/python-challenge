# Write a function called check_duplicates that takes a list of
# strings as an argument. The function should check if the list has
# any duplicates. If there are duplicates, the function should return
# the duplicates. If there are no duplicates, the function should
# return "No duplicates". For example, the list of fruits below
# should return apple as a duplicate and list of names should
# return "no duplicates".
# fruits = ['apple', 'orange', 'banana', 'apple']
# names = ['Yoda', 'Moses', 'Joshua', 'Mark']


def check_duplicates():
  fruits = ['apple', 'orange', 'banana', 'apple']
  newList = []
  dupList = []
  for fruit in fruits:
    if fruit not in newList: newList.append(fruit)
    else: dupList.append(fruit)
  print(f'Unique Item List: {newList}')
  print(f'List of duplicates{dupList}')
