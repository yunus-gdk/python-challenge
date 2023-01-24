# Write a function called equal_strings.
# The function takes two strings as arguments and compares them.
# If the strings are equal
# (if they have the same characters and have equal length),
# it should return True, if they are not, it should return False.
# For example, ‘love’ and ‘evol’ should return True.


def equal_strings(str1, str2):
  
  if len(str1) == len(str2): 
    sorted_chars1 = sorted(str1)
    sorted_string1 = ''.join(sorted_chars1)
    sorted_chars2 = sorted(str2)
    sorted_string2 = ''.join(sorted_chars2)
    if sorted_string1 == sorted_string2: print(True)
    else: print(False)
  
  else: print(False)
  
equal_strings("lovee", "evola")
