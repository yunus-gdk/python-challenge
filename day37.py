# Create a function called count_the_vowels. The function 
# takes one argument, a string, and returns the number of vowels
# in the string. For example, ‘hello’ should return 2 vowels. If a 
# vowel appears in a string more than once it should be counted 
# as one. For example, ‘saas’ should return 1 vowel. Your code 
# should count lowercase and uppercase vowels

from collections import defaultdict
import re

def count_the_vowels(mot):
    d = defaultdict(int)
    for lettre in mot:
        if re.match(r'[aeiouy]', lettre):
            d["voyelle"]+=1
        else:
            d["consonne"]+=1
    print(d.items())

count_the_vowels("saas")
