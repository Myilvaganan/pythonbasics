"""
============================================================================================================================================================================================
A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).
However, a set itself is mutable. We can add or remove items from it.
Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

Method	----------------------------------- Description

add()	----------------------------------> Adds an element to the set
clear()	----------------------------------> Removes all elements from the set
copy()	----------------------------------> Returns a copy of the set
difference()    -------------------------->	Returns the difference of two or more sets as a new set
difference_update() ---------------------->	Removes all elements of another set from this set
discard()	------------------------------> Removes an element from the set if it is a member. (Do nothing if the element is not in set)
intersection()	--------------------------> Returns the intersection of two sets as a new set
intersection_update()	------------------> Updates the set with the intersection of itself and another
isdisjoint()    -------------------------->	Returns True if two sets have a null intersection
issubset()  ------------------------------>	Returns True if another set contains this set
issuperset()	--------------------------> Returns True if this set contains another set
pop()	----------------------------------> Removes and returns an arbitrary set element. Raises KeyError if the set is empty
remove()	------------------------------> Removes an element from the set. If the element is not a member, raises a KeyError
symmetric_difference()	------------------> Returns the symmetric difference of two sets as a new set
symmetric_difference_update()	----------> Updates a set with the symmetric difference of itself and another
union()	----------------------------------> Returns the union of sets in a new set
update()	------------------------------> Updates the set with the union of itself and others

Function	------------------------------- Description

all() ------------------------------------>	Returns True if all elements of the set are true (or if the set is empty).
any()	----------------------------------> Returns True if any element of the set is true. If the set is empty, returns False.
enumerate()------------------------------->	Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
len()	----------------------------------> Returns the length (the number of items) in the set.
max()	----------------------------------> Returns the largest item in the set.
min()	----------------------------------> Returns the smallest item in the set.
sorted()	------------------------------> Returns a new sorted list from elements in the set(does not sort the set itself).
sum()	----------------------------------> Returns the sum of all elements in the set.
============================================================================================================================================================================================
"""

# Different types of sets in Python
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# {1, 2, 3}
# {1.0, (1, 2, 3), 'Hello'}

# set cannot have duplicates
# Output: {1, 2, 3, 4}
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1, 2, 3, 2])
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.

# my_set = {1, 2, [3, 4]}

# Distinguish set and dictionary while creating empty set

# initialize a with {}
a = {}

# check data type of
print(type(a))

# initialize a with set()
a = set()

# check data type of
print(type(a))

# <class 'dict'>
# <class 'set'>


# initialize my_set
my_set = {1, 3}
print(my_set)

# my_set[0]
# if you uncomment the above line
# you will get an error
# TypeError: 'set' object does not support indexing

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8})
print("line-77", my_set)

# Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

# my_set.remove(2)

# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
my_set.pop()
print(my_set)

# clear my_set
# Output: set()
my_set.clear()
print(my_set)

# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)

# Intersection of sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)

# Difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A - B)

# Symmetric difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)

# Returns True if all elements of the set are true (or if the set is empty).
print(all(A))  # True

new_set1 = {1, 0, 34, 456}
print("ALL", all(new_set1))  # False

# Returns True if any element of the set is true. If the set is empty, returns False.
print("ANY", any(new_set1))  # True

# Returns the length (the number of items) in the set.
print(len(new_set1))  # 456

new_set2 = {"test", "sample", "myilvaganan", "python"}
# Returns the largest item in the set.
print(max(new_set2))  # test

# Returns the smallest item in the set.
print(min(new_set1))      # 0

#  Returns a new sorted list from elements in the set(does not sort the set itself).
print(sorted(new_set1)) # [0, 1, 34, 456]
print(sorted(new_set2)) # ['myilvaganan', 'python', 'sample', 'test']

# Returns the sum of all elements in the set.
print(sum(new_set1)) # 491

# Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
print(enumerate(new_set1))
for i in enumerate(new_set1):
    print(i)

"""
----------------
Output
----------------
(0, 0)
(1, 1)
(2, 34)
(3, 456)
"""

# Frozensets
"""
==========================================================================================================================================
Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. 
While tuples are immutable lists, frozensets are immutable sets.
Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are hashable and can be used as keys to a dictionary.
Frozensets can be created using the frozenset() function.
This data type supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), 
symmetric_difference() and union(). Being immutable, it does not have methods that add or remove elements.
==========================================================================================================================================
"""
# initialize A and B
frozensetA = frozenset([1, 2, 3, 4])
frozensetB = frozenset([3, 4, 5, 6])

print(frozensetA)
print(frozensetB)
