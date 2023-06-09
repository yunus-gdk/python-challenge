# Write a function called count that takes one argument a string,
# and returns a dictionary of how many times each element appears in the string.
# For example, ‘hello’ should return:
# {‘h’:1,’e’: 1,’l’:2, ‘o’:1}.

from collections import defaultdict

def count(mot):
    d = defaultdict(int)
    for lettre in mot:
        d[lettre]+=1
    print(d.items())

# count(input("Enter a string: "))
mot = "yunus"
count(mot)
