# Write a function called prime_numbers.
# This function asks a user to enter a number (integer) as an argument
# and returns a list of all the prime numbers within its range.
# For example,
# if user enters 10, your code should return [2, 3, 5, 7] as prime numbers.

number = int(input("Enter an integer: "))


def prime_numbers(number):
  for i in range(2, number):
    if (number % i) == 0:
      return False
  return True


prime_numbers(number)
