
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

# to get rid of an empty line at the end of each line(after each Name)
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
names = []  #  it's quite a common technique to fetch data, put it into a temporary
            #  variable and using certain features of the type of variable we can
            #  manipulate it

with open("names.txt") as file:
  for line in file:
    names.append(line.rstrip())

for name in sorted(names):    # sorting the list before iterating over it
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
#  Do we actually want to make changes to the data we are iterating over?

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

# By default sorted function sorts data in the alphabetic order A -> Z and 0 -> 9
# But you can pass as a parameter to the sorted(obj, reverse = True)reversed order 
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

# you can look for a specific value or specific data in a file by iterating through it using the for loop
# and pass the condition for your search.



#################################################

# .txt files are good enough for keeping some simple data
# for storing "more complex" sets of data, programmers (by convention) use CSV-files
# CommaSeparetedValues
# and it's a very common convention to store multiple pieces of information that are related in the same file. 

# In these .csv files you can see a sort of two-dimentional file
# row by row we have our names with releted to these names infornation (the name of the department in this case)
# you can think about this commas as representing a column
# and it turns out, these CSV files are very commonly used when you use something like Microsoft Exel, Apple Numbers,
# or Google spread sheets, and you want ot export the data to share with someone else as a CSV file.
# or conversely, if you want to inport a CSV file into your prefered spreadsheet software,
# you can do that as well.

# So, CSV is very common, very simple text format, that just separetes values with commas, 
# and different types of values, ultimately with new lines as well.

# In this case these names and departments are not all on one line.
# We can have an access to both types of value separately

"""
with open("names.csv") as file:     # "file" is just a randomly named variable
  for line in file:
    row = line.rstrip().split(",")  # this returns you a list of all of the individual parts to the left and to the right of those commas.
                                    # it's common paradigm when you're iterating over a file, specifically a CSV,
                                    # to think of each line as being a row and each of the values therein separated by commas 
                                    # as columns.
    print(f"{row[0]} works at {row[1]}")  
"""

# Actually if you want to, in Python, change a line in the file and not just append to the end. You would have to 
# implemet that logic yourself. So, for instance, you could imagine now opening the file,
# and reading aii of the contents in, then maybe iterating over each of those lines.
# As soon as you reach the current name == eg Sam, you could change his department to Engineering.
# Then it would up to you to write all of thouse changes back to the file.
# So, in that case you might want to, in simplest form, read the file once and let it close.
# Than open it again, but open for writing, and change the whole file.
# Its' not really possible  or easy to go in and change just part of the file, though you can do it.
# It's easier to read the whole file, make your changes in memory, and then then write the whole file out.
# But for a larger files wher e that might be quite slow.



# Instead of loading all of those variables into a list, you can actually "unpack" that whole sequence at once.
# In our case split will return a list, but you know in advance that it's going to return two values in a list,
# the first and the second. You don't have to load them all into a variable that itself is a list.
# You can actually unpack them simultaneously into two variables, name and dep

"""
with open("names.csv") as file:     
  for line in file:
    name, dep = line.rstrip().split(",")  
    print(f"{name} works at {dep}")
"""

# This is a nice Python technique to not only create, but assign, automatically,
# in parallel two varibles at once, rather than just one.


# If you want to sort the list of output you can actually 
# create an empty list, append to this new list and intead of dealing with these full phrases
# we were only dealing with names. For this we need to create an empty list,
# append values to the list and before actually printing the sentence, 
# we're going to store it temporarily in a list. So, we can accumulate all of these sentences
# and then sort them later.
#  
"""
names = []

with open("names.csv") as file:
  for line in file:
    name, dep = line.rstrip().split(",")
    names.append(f"{name} works at {dep}")

for name in sorted(names):
  print(name)

"""

# technicly even though we want to sort this by name we actually
# sort this by whole English sentences.
# It's not wrong, it's achieving the intended result, but it's not really
# well designed because you're just getting lucky that English is reading from left to right. 
# and therefore, when you print this out, it's sorting properly.

# It would be better to come up with a technique for sorting by the employees names, not by some English sentence 
# that we constructed above in line 230.
# 
# To achieve this we need to do the following:
# we're going to need to collect information about each employee before we aseemble that sentence. 
#
# 
# 
# 
# 
# Let's do this:
# Recall that Python supports dictionaries.
# Dictionaries are just collections of keys and values. So we can associate something with something else,
# like a name with department.
# That really is a dictionary.
# Let's create a dictionary that stores this association of name with department.
#    

"""
names = []

with open("names.csv") as file:
  for line in file:
    name, dep = line.rstrip().split(",")
    employee = {}
    employee["name"] = name
    employee["dep"] = dep
    names.append(employee) # why have we actually done this?
                           # we've admittedly made our code more complicated.
                           # It's more lines of code, but we've now collected all of 
                           # the information we have about employees while still keeping
                           # track - what's a name, what's a department.
                           # The list has all of the employees' names and departments together
                           # 
                           # Why have we done this?
                           # 
                           # well, let's  just do something simple:
for employee in names:
  print(f"{employee['name']} works at {employee['dep']}")

"""

# inside of this F string, we're using curly brackets, as always.
# Inside of those we're using the name of a variable as always.
# But then we're not using an index of the variable like 0 or 1 or..
# because this is a dictionary now, not a list.
# 
# But why are we using these single quotes to surround department or name?
#    



# If you're in the habit  of creating an empty dictionary, like in this line 267,
# and then immediately putting into two keys, name and department, you can do it all at once 
#
"""
names = []

with open("names.csv") as file:
  for line in file:
    name, dep = line.rstrip().split(",")
    employee = {"name": name, "dep": dep}  # here we creating a new non-empty dicionary
                                          # containing a name key,and a department value 
    names.append(employee)

for employee in names:
  print(f"{employee['name']} works at {employee['dep']}") 

"""
# it still works but the're still not quite actually sorted 

# We need some mechanism now of sorting thoue employees.
# But unfortunatelly we can't do this. We can't sort all of these employees now because employees are not names
# like they were before. They aren't sentences like they were before.
# Each of the enployees is a dictionary now, and it's not obvious 
# how you would sort a dictionary inside of a list.
# 
# \
# So, ideally what do we want to do?
# 
# If at the moment we hit the line 307 (where we're starting iterating through),
# we have a list of all these employees, and inside that list is one dictionary per emploee,
# and each of these dictionaries has two keys, name and dep,
# wouldn't it be nice if there were way in code to tell Python, sort this list 
# by looking at this key in each dictionary?
# 
# Because that would give us the ability to sort either by name, or even by house, 
# or by any other field that we add to that file.
# 
# We can tell the sorted function not just to reverse things or not.
# It takes another positional - it takes another named parameter called key, 
# where you can specify what key should be used in order to sort some list of dictionaries.
# 
# 
# To do this we're going to first define a function - temporarily, for now - called get_name.
# And this function's purpose in life, given a employee, is to simply return the employee name 
# from a particular dictionary.
# and that's it. That's the sole purpose of this function in life
# 
# def get_name(employee):
#  return employee["name"]


# What do we now want to do?
# 
# We can change sorted to say, use a key that's equal to whatever the return value of get_name is.
#  
# And this now is a feature of Python.
# Python allows you to pass functions as arguments into other functions.
# So, get_name is a funtion, sorted is a function.
# and we are passing in get_name to sorted as the value of that key parameter.
# 
# Why are we doing that?
# 
# If you think of the get_name function, it's just a block of code that will get the name of an employee.
# That's handy because that's the capability that sorted needs.
# When given a list of staff, each of which is a dictionary, sorted needs to konw, how do I get the name of the employee?
# In order to do alphabetical sorting for you.
# 
# The The authors of Python didn't know that we were going to be creating employees here in this class.
# So what did they do?
#  
# They instead built into the sorted function this named paramater key that allows us to tell their function sorted 
# how to sort this list of dictionaries.  
#    
"""
names = []

with open("names.csv") as file:
  for line in file:
    name, dep = line.rstrip().split(",")
    employee = {"name": name, "dep": dep} 
    names.append(employee)


def get_name(employee):
  return employee["name"]

for employee in sorted(names, key = get_name):
  print(f"{employee['name']} works at {employee['dep']}") 

"""


# now we have a sorted list of output.
# 
# Why?
# 
# Because now that list of dictionaries has all been sorted by employees' name. 
# We can reverse it by passing an additional parameter as we were doing before reverse = True     
# 
# if we need/want to sort this, for instance, by department we can create a similar function
# get_dep:
# 
# def get_dep(employee):
#   return employee["dep"] 

# and pass it as a key insted of get_name
"""
names = []

with open("names.csv") as file:
  for line in file:
    name, dep = line.rstrip().split(",")
    employee = {"name": name, "dep": dep} 
    names.append(employee)


def get_dep(employee):
  return employee["dep"]

for employee in sorted(names, key = get_dep, reverse = True):
  print(f"{employee['name']} works at {employee['dep']}") 

"""
# These are examples of creating sorting algorithms from scratch. 
# With other functions or libraries, some of this could be made more easily done.
# 
# 
# as I metioned before "The documentation is your friend!" 
# docs.python.org

# Some of this could be made easier.

# NOTE!!! that as a value to the parameter key we need to pass a VALUE
# 
# In our case when you pass in a function get_name or get_dep into the sorted function as a value of key,
# that function is automatically called by the sorted function for you 
# on each of the dictionaries in the list.
# And it uses the return value of them to decide what string to actually use to compare in order to decide
# which is aplphabeticlally correct.

# So you you need to pass this function by name, you don't need to pass in paretheses at the end,
# is called by by the sorted function


###########################

# 