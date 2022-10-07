def removeExtraSpaces(func):
    def inner(value):
        if type(value) == int:
            return "Sorry! Provide Valid String"
        value = value.strip()
        return func(value)

    return inner


def upperCase(func):
    def inner(value):
        if type(value) == int:
            return "Sorry! Provide Valid String"
        return func(value)

    return inner


@removeExtraSpaces
@upperCase
def convertString(a):
    return a.upper()


print(convertString("           hi! i am myilvaganan.      "))
print(convertString(2))


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Myilvaganan")
