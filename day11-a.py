# Write a function called swap_values.
# This function takes a list of numbers and swaps the first element with the last element.
# For example, if you pass [2, 4,67, 7] as a parameter,
# your function should return [7, 4, 67, 2].

def swap_values(liste):
    first_item = liste[0]
    last_item = liste[-1]
    liste.pop(0)
    liste.pop(-1)
    liste.append(first_item)
    liste.insert(0, last_item)
    print(liste)

swap_values([2, 4, 67, 7])
