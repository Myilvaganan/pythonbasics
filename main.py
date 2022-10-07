# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    course = "Python For Beginners"
    print(course[1:])  # Returns from 1 to the last - ython For Beginners
    print(course[2:9])  # Returns from 2 to 8 - thon Fo
    print(course[1:-1])  # Returns from 1 to -2 - ython For Beginner
    message = f"{course} {name}"
    print(message)  # Python For Beginners PyCharm
    print(len(message))  # Return Length of the string
    print(course.upper())  # PYTHON FOR BEGINNERS
    print(course.lower())  # python for beginners
    print(course)  # Python For Beginners
    print(course.find("B"))  # 11 if exists return the index
    print(course.find("Z"))  # -1 if not exists return the index
    print(course.find("Beginners"))  # 11 Return the starting index
    print(course.replace("Beginners", "Absolute Beginners"))  # Python For Absolute Beginners
    print(course.replace("n", "z"))  # Replace all 'n' to 'z' - Pythoz For Begizzers
    print('Python' in course)  # True Case Sensitive - return always boolean
    print(course.lower().title())  # Python For Beginners Capitalize
    #  Arithmetic Expressions
    print(2 + 2)  # 4
    print(2 - 2)  # 0
    print(2 / 4)  # 0.5
    print(10 // 3)  # 3
    print(10 * 3)  # 30
    print(10 ** 3)  # 1000 Power of 3


class SkandaMyil:
    def __init__(self, name):
        self.name = name

    def func1(self):
        print(self, "My First Fn Inside Class")


A = SkandaMyil("Myilvaganan")
print(A.name)  # Myilvaganan
print(A.func1())  # <__main__.SkandaMyil object at 0x101122fd0> My First Fn Inside Class


def scopes():
    def local_func():
        name = 'LOCAL_VARIABLE'
        print("5", name)

    def non_local():
        nonlocal name
        name = 'NON_LOCAL_VARIABLE'

    def global_func():
        global name
        name = 'GLOBAL_VARIABLE'

    name = "LOCAL"
    print("1", name)
    local_func()
    print("2", name)
    non_local()
    print("3", name)
    global_func()


scopes()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
