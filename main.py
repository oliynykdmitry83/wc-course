"""names = []

for _ in range(3):
  names.append(input("What is your name? "))
  
for name in sorted(names):
  print(f"Hello, {name}")
"""

#writing file

"""
name = input("What is your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()  

"""

# appending to the ile

"""

name = input("What is your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()  


"""

#$ rm names.txt // Removes file //   works in CLI like built-in terminal or any other shells

"""
name = input("What is your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

"""

# to close the file automaticly Python has built-in feature
# named "with ... as ..."

"""
name = input("What is your name? ")

with open("names.txt", "a") as file:
  file.write(f"{name}\n")

"""

# reading a file:

with open("names.txt", "r") as file:
  lines = file.readlines() 
  # readlines() - reads all lines of the file and return it as a list
  # rstrip() - removes whitespaces from the end of each line
  # split() - splits each line into a list of words
  # you can find ALL built in funcs in docs.python.org or other alterniative resources
  # e.g. w3school or so...

for line in lines:
  print("Hello, ",  line)

# to rid of an empty line at the end of each line(after each Name)
# you can pass the third arugment to print() as end=""
# or you can use rstrip() to remove whitespaces from the end of each line
  
# if you want to print the whole file at once:
                        