from typing import Any, Callable


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

"""
--------------------------------------HIGHER ORDER FUNCTIONS-----------------------------------------------------
FUNCTIONS ARE OBJECTS, THEY CAN BE  PASSED TO OTHER FUNCTIONS AND FUNCTIONS CAN ALSO RETURN FUNCTIONS
THIS DATA TYPE IS CALLED CALLABLE, ONE WHICH CAN BE CALLED OR INVOKED
------------------------------------------------------------------------------------------------------------------
"""


def goodMorning(name: str) -> str:
    return "GOOD MORNING!" + " " + name


def goodEvening(name: str) -> str:
    return "GOOD EVENING!" + " " + name


def goodNight(name: str) -> str:
    return "GOOD NIGHT!" + " " + name


def generateStatement(name: str, greeter: Callable[[str], str]):
    msg = greeter(name)
    print(msg)


generateStatement("Myilvaganan", goodNight)  # GOOD NIGHT! Myilvaganan
generateStatement("Myilvaganan", goodEvening)  # GOOD EVENING! Myilvaganan
generateStatement("Myilvaganan", goodMorning)  # GOOD MORNING! Myilvaganan

"""
--------------------------------------HIGHER ORDER FUNCTIONS-----------------------------------------------------
FUNCTIONS RETURNING FUNCTIONS
------------------------------------------------------------------------------------------------------------------
"""


def addBy5(num: int) -> Callable[[], int]:
    def by_5() -> int:
        return num + 5

    return by_5


SUM = addBy5(5)
print(SUM)  # <function addBy5.<locals>.by_5 at 0x10ba90ca0>
print(SUM())  # 10


def unique_adder(num1: int) -> Callable[[int], int]:
    def adder(num2: int) -> int:
        return num1 + num2 - 2

    return adder


new_adder = unique_adder(10)
print(new_adder)  # <function unique_adder.<locals>.adder at 0x10b07bdc0>
# print(new_adder()) # <function unique_adder.<locals>.adder at 0x10cec4dc0> adder() missing 1 required positional argument: 'num2'
print(new_adder(100))  # 108

"""
--------------------------------------HIGHER ORDER FUNCTIONS-----------------------------------------------------
LAMBDA
condense in to single statement
------------------------------------------------------------------------------------------------------------------
"""

addTwoNum: Callable[[int, int], int] = lambda num1, num2: num1 + num2
print(addTwoNum(1, 3))  # 4

minusTwoNum: Callable[[int, int], int] = lambda num1, num2: num1 - num2
print(minusTwoNum(1, 3))  # -2

multiplyThreeNum: Callable[[int, int], int] = lambda num1, num2: num1 * num2
print(multiplyThreeNum(1, 3))  # 3



