# Create three functions.
# The first called add_hash takes a string and adds a hash (#) between the words.
# The second function called add_underscore removes the hash (#) and replaces it with an underscore "_"
# The third function called remove_underscore, removes the underscore and replaces it with nothing.
# if you pass ‘Python’ as an argument for the three functions, and you call them at the same time like:
# print(remove_underscore(add_underscore(add_hash('Python'))))
# it should return ‘Python’.

listStr = []

def add_hash(strAdd):
  for i in strAdd:
    listStr.append(i)
    listStr.append("#")
  listStr.pop()
  print(''.join(listStr))
  return ''.join(listStr)
  
def add_underscore(strAdd):
  print(strAdd.replace("#","_"))
  return strAdd.replace("#","_")
  
def remove_underscore(strAdd):
  return strAdd.replace("_","")

print(remove_underscore(add_underscore(add_hash('Yunus'))))

