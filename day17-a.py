# names = ["Peter", "Jon", "Andrew"]
# Write a function called sort_length
# that takes a list of strings as an argument,
# and sorts the strings in ascending order according to their length.
# For example, the list above should return:
# ['Jon', 'Peter', 'Andrew']
# Do not use the built-in sort functions

def sort_length(names):
    names_dict = {len(name): name for name in names}
    print(names_dict)
    # {'Peter': 5, 'Jon': 3, 'Andrew': 6}
    names_list = list(names_dict.keys())
    names_list.sort()
    sorted_dict = {i: names_dict[i] for i in names_list}
    print(sorted_dict)
    

sort_length(["Peter", "Jon", "Andrew"])
