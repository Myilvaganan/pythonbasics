lists = ["Myil", "vaganan", "developer"]  # Create List
empty_list = []  # Create Empty List
mixed_data_types = [1, "string", False, {'a': 4}]  # Contains mixed data types
nested_list = [1, 4, ["string", {'a': 4}], True, 5]
#  Index
print(lists[0])  # 'Myil'
print(lists[1])  # 'vaganan'
# print(lists.index("1"))  # Error : ValueError: '1' is not in list
print("1" in lists)  # False
print(nested_list[2][1])  # {'a': 4}
# print(lists[2.0])  Error! Only integer can be used for indexing
print(lists[-1])  # developer negative indexing
new_list = ['m0', 'y1', 'i2', 'l3', 'v4', 'a5', 'g6', 'a7', 'n8', 'a9', 'n10']
print(new_list[2:8])  # ['i2', 'l3', 'v4', 'a5', 'g6', 'a7'] - Excluded 8th index
print(new_list[4:])  # ['v4', 'a5', 'g6', 'a7', 'n8', 'a9', 'n10']
print(new_list[:4])  # ['m0', 'y1', 'i2', 'l3']
new_list[0] = "new_element"
print(new_list)  # ['new_element', 'y1', 'i2', 'l3', 'v4', 'a5', 'g6', 'a7', 'n8', 'a9', 'n10']
new_list[2:6] = ["new2", "new3", "new4", "new5"]
print(new_list)  # ['new_element', 'y1', 'new2', 'new3', 'new4', 'new5', 'g6', 'a7', 'n8', 'a9', 'n10']
# Concatenating and repeating lists
odd = [1, 3, 5]
print(odd + [9, 7, 5])  # [1, 3, 5, 9, 7, 5]
print(["myil"] * 3)  # ['myil', 'myil', 'myil']
odd.insert(2, 4)
print(odd)  # [1, 3, 4, 5]
odd[1:3] = ["a", "b", "c"]
print(odd)  # [1, 'a', 'b', 'c', 5]
odd.append("appending new element")
print(odd)  # [1, 'a', 'b', 'c', 5, 'appending new element'] - to the last of the list
odd.pop(2)
print(odd)  # [1, 'a', 'c', 5, 'appending new element'] -popped element in index 2
del odd[1]
print(odd)  # [1, 'c', 5, 'appending new element'] - deleted index 1
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
my_list.remove('p')
# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list)  # ['r', 'o', 'b', 'l', 'e', 'm']
# Output: 'o'
print(my_list.pop(1))
# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list)
# Output: 'm'
print(my_list.pop())
# Output: ['r', 'b', 'l', 'e']
print(my_list)
my_list.clear()
# Output: []
print(my_list)
'''
append()	adds an element to the end of the list
extend()	adds all elements of a list to another list
insert()	inserts an item at the defined index
remove()	removes an item from the list
pop()	returns and removes an element at the given index
clear()	removes all items from the list
index()	returns the index of the first matched item
count()	returns the count of the number of items passed as an argument
sort()	sort items in a list in ascending order
reverse()	reverse the order of items in the list
copy() 	returns a shallow copy of the list
'''