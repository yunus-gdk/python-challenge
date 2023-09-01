# names = ["Peter", "Jon", "Andrew"]
# Write a function called sort_length
# that takes a list of strings as an argument,
# and sorts the strings in ascending order according to their length.
# For example, the list above should return:
# ['Jon', 'Peter', 'Andrew']
# Do not use the built-in sort functions

def sort_length(names):
    names_dict = {len(name): name for name in names}
    names_list = final_list = []
    names_list = list(names_dict.keys())
    names_list.sort()
    sorted_dict = {i: names_dict[i] for i in names_list}
    print(sorted_dict)
    for value in sorted_dict.values():
        final_list.append(value)
    print(final_list)    

sort_length(["Peter", "Jon", "Andrew"])
