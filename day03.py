# Write a function called register_check that checks how many
# students are in school. The function takes a dictionary as a
# parameter. If the student is in school, the dictionary says ‘yes’. If
# the student is not in school, the dictionary says ‘no’. Your
# function should return the number of students in school. Use the
# dictionary below. Your function should return 3.


def register_check():
  register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
  nbYes = 0
  for item in register.values():
    if item == "yes": nbYes += 1
  print(f'{nbYes}')
