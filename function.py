from typing import Any


def func(name: str) -> str:
    return f"I am {name}"


print(func("Myilvaganan"))  # I am Myilvaganan


def func(name: Any) -> str:
    return f"I am {name}"


print(func(False))  # I am False

"""
**args and **kwargs
Use it when you are not sure of how many arguments we receive
"""

# ----- UnPacking ----

first, second = "name", "same"

# Similar to Rest Operator in Javascript ES6+
firstEl, *rest = ["one", 'two', 'three', 'four', 'five']
print(firstEl, rest)  # one ['two', 'three', 'four', 'five']

# Similar to Spread Operator in Javascript ES6+
specs = {"age": 26, "address": "Salem", "pincode": "636012"}
addName = {"name": "Myilvaganan", **specs}

print(addName)  # {'name': 'Myilvaganan', 'age': 26, 'address': 'Salem', 'pincode': '636012'}


def unknown_elements(*args: str) -> Any:
    for i in args:
        print(i)


unknown_elements("a", "b", "c", "d", "e")
"""
a
b
c
d
e
"""


# Keyword args

def unknown_pairs(**kwargs: Any) -> None:
    for key, value in kwargs.items():
        print(key, value)


unknown_pairs(name="MYIL", age=24, address='Salem')
"""
name MYIL
age 24
address Salem
"""


# Combined Func

def combined(element: str, *args: str, **kwargs: str) -> None:
    print(element)  # TEST
    print(args)  # ('TEST1', 'TEST2', 'TEST3', 'TEST4', 'TEST5')
    print(kwargs)  # {'TEST6': '6', 'TEST7': '7', 'TEST8': '8', 'TEST9': '9', 'TEST10': '10'}


combined("TEST", "TEST1", "TEST2", "TEST3", "TEST4", "TEST5", TEST6="6", TEST7="7", TEST8="8", TEST9="9", TEST10="10")
