# enum
from enum import Enum


class Colors(Enum):
    red = 1
    green = 2
    blue = 3


# list of list initialization
x = [[] for _ in range(3)]
# same as:
y = []
for i in range(3):
    y.append([])

# list of lists with init
z = [[None] * 2 for _ in range(3)]

# copy a list:
my_list = [1, 2]
new_list = my_list.copy()  # same as: new_list = old_list[:]

# spreading collections into another collection
my_set = {*my_list}  # same as: my_set = set(my_list)

# flattening a list of sublists:
flat_list_ = [item for sublist in x for item in sublist]
# is same as:
flat_list = []
for sublist in z:
    for item in sublist:
        flat_list.append(item)

# in lambda/function:
def flatten(list_of_list): return [item for sublist in list_of_list for item in sublist]

# for dictionary, we can have
d = {'a': 1, 'b': 2}
print(d.keys(), d.values(), d.items())

# check for key existence:
d = {"key1": 10, "key2": 23}
if "key1" in d:
    print("this will execute")
if "nonexistent key" in d:
    print("this will not")


# class method/variable example:
class Person:
    age = 25

    def print_age(cls):
        print('The age is:', cls.age)

# There are instance methods (the normal ones), which have an instance object referenced as self.
# Then there are class methods (using @classmethod) which have a reference to the class object as cls.
# And finally there are static methods (declared with @staticmethod) which have neither of those references.
# Static methods are just like functions at module level, except they live in the class' name space
