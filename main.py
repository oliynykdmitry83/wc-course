
"""
names = []

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

#$ rm names.txt // Removes file // works in CLI like built-in terminal or any other shells

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

"""
with open("names.txt", "r") as file:
  lines = file.readlines() 
  # readlines() - reads all lines of the file and return it as a list
  # rstrip() - removes whitespaces from the end of each line
  # split() - splits each line into a list of words
  # you can find ALL built in funcs in docs.python.org or other alterniative resources
  # but

for line in lines:
  print("Hello, ",  line)

# to rid of an empty line at the end of each line(after each Name)
# you can pass the third arugment to print() as end=""
# or you can use rstrip() to remove whitespaces from the end of each line

"""
# you can rewrite this code in a little bit different/"Pythonic"/more compact way:

"""
with open("names.txt", "r") as file:  # open file for reading
  for line  in file:                  # iterativly read each line
    print("Hello, ", line.rstrip())   # print each line and remove whitespaces

"""

#  to sort data from this file we need to read it first, then put in a list and sort it
#  note! that we are fetching data from a file and put everything into a variable and 
#  manupulating it

"""
names = []  #  it's quite a common technicue to fech data, put it into a temprorary
            #  varible and using certain features of the type of varible we can
            #  manipulate it

with open("names.txt") as file:
  for line in file:
    names.append(line.rstrip())

for name in sorted(names):    # sorting the list before itrating over it
  print(f"Hello, {name}")  

"""


# we can do it in a more compact way: 
# it looks much more "Pythonic" :)

"""
with open("names.txt") as file:
  for line in sorted(file):
    print("Hello,", line.rstrip())

"""

#  BUT in this case YOU have to answer a question:
#  Do we actially want to make changes to the data we are iterating over?

#  docs.python.org/3/library/function.html#sorted
#  here you can find all possible ways of sorting 

"""
names = []

with open("names.txt") as file:
  for line in file:
    names.append(line.rstrip())

for name in sorted(names):    # sorting the list before itrating over it
  print(f"Hello, {name}")
"""

# By default sorted function sorts data in the alphabetic order A -> Z and 1 -> 10
# But you can puss as a parameter to the sorted(obj, reverse = True)reversed order 
# as I mentioned before: "The documentation is your friend!" 
# docs.python.org

# by default it looks like: sorted(iterable, /, *, key = None, reverse = False)
# key - param we will talk about it later


"""names = []

with open("names.txt") as file:
  for line in file:
    names.append(line.rstrip())

for name in sorted(names, reverse = True): 
  print(f"Hello, {name}")

"""

# you can look for specific value or specific data in a file by iterating throug using the for loop
# and pass the codition for your search.



#################################################

# .txt files are good enougt for keeping some simle data
# for storing "more complex" sets of data programmers (by convention) use CSV-files
# CommaSeparetedValues
# and it's a very common convention to store multiple pieces of information that are related in the same file. 

# in these .csv files you can see a sort of two-dimentional file
# row by row we have our names with releted to these names infornation (the name of the department in this case)
# you can think about this commas as representing a column
# and it turns out, these CSV files are very commonly used when you use something like Microsoft Exel, Apple Numbers,
# or Google spread sheets, and you want ot export the data to share with someone else as a CSV file.
# or conversely, if you want to inport a CSV file into your prefered spreadsheet software,
# you can do that as well.

# So, CSV is very common, very simple text format, that just separetes values with commas, 
# and different types of values, ultimately with new lines as well.

# In this case these names and departments they're not all on one line.
# We can have an access to both type of value separately


with open("names.csv") as file:     # file it's just a random named variable
  for line in file:
    row = line.rstrip().split(",")  # this returns you a list of all of the individual parts to the left and to the right of those commas.
                                    # it's coomon paradigm when you're iterating over a file, specificly a CSV,
                                    # it's common to think of each line if it as being a row and each of the values therein separated by commas 
                                    # as columns.
    print(f"{row[0]} works in {row[1]}")  




