# You work for a school and your boss wants to know how many
# female and male students are enrolled in the school.
# The school has saved the students in a list. Your task is to write a code that
# will count how many males and females are in the list. Here is a list below:
# students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
# Your code should return a list of tuples. The list above should return:
# [(‘Male’,7), (‘female’,6)

students = [
  'Male', 'Female', 'female', 'male', 'male', 'male', 'female', 'male',
  'Female', 'Male', 'Female', 'Male', 'female'
]

lowercaseList = []
maleList = []
femaleList = []
genderList = ["Male", "female"]
resultList = []


def number_students():
  for student in students:
    lowercaseList.append(student.lower())
  print(lowercaseList)
  for gender in lowercaseList:
    if gender == 'female': femaleList.append(gender)
    else: maleList.append(gender)

  resultList = [len(maleList), len(femaleList)]
  print(list(zip(genderList, resultList)))


number_students()
