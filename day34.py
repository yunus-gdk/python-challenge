# In this challenge, copy the text below and save it as a CSV file.

# Python was released in 1991 for the first time. Python 2 was released in 2000 and introduced new features, such as list comprehensions and a cycle-detecting garbage collection system (in addition to reference counting). Python 3 was released in 2008 and was a major revision of the language that is not completely backward-compatible.

# Save it in the same folder as your Python file. Save it as python.csv.
# Write a function called just_digits that reads the text from the CSV file
# and returns only digit elements from the file.
# Your function should return 1991, 2, 200, 3, 2008 as a list of strings.

import csv


def just_digits():
  j = 0

  with open("./fileday34.csv", 'r') as file:
    csvreader = csv.reader(file, delimiter=' ')

    for i in csvreader:
      while j <= len(i):
        j += 1
        if i[j].startswith(('1', '2', '3')):
          print(i[j])
  file.close()


just_digits()
