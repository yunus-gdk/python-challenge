# Write a function called password_validator.
# The function asks the user to enter a password.
# A valid password should have at least one upper letter, one lower letter, and one number.
# It should not be less than 8 characters long.
# When the user enters a password, the function should check if the password is valid.
# If the password is valid, the function should return the valid password.
# If the password is not valid, the function should tell the users the errors in the password and prompt the user to enter another password.
# The code should only stop once the user enters a valid password. (use while loop)


def password_validator():
  password = input(
    "Enter a password with 1 upper letter, 1 lower letter, 1 number and not be less than 8 characters long: "
  )

  nbDigit = 0
  nbLower = 0
  nbUpper = 0
  for i in password:
    if i.isdigit(): nbDigit += 1
  for i in password:
    if i.islower(): nbLower += 1
  for i in password:
    if i.isupper(): nbUpper += 1

  if ((nbDigit and nbLower and nbUpper) > 0
      and (nbDigit + nbLower + nbUpper > 7)):
    print(f"the password {password} is correct :)")
    return True
  else:
    return False


while not password_validator():
  password_validator()
