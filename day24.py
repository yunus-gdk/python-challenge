# Create a function called average_calories that calculates the
# average calories intake of a user.
# The function should ask the user to input their calories intake
# for any number of days
# and once they hit ‘done’ it should calculate
# and return the average intake.


def average_calories():
  listCalorie = []
  while True:
    calorie_input = input(
      "Enter your calories intake for the day (or 'done' to finish): ")
    if calorie_input == 'done':
      break
    try:
      calorie = int(calorie_input)
      listCalorie.append(calorie)
    except ValueError:
      print("Invalid input, please enter a number or 'done' to finish.")

  average = sum(listCalorie) / len(listCalorie)
  print(int(average))


average_calories()
