var: int = 100


def get_local_var():
    var: int = 900
    print(var)


def add_var():
    global var
    var += 100
    print(var)


def int_local_num():
    new = var + 100
    print(new)


print("LINE 20", var)  # LINE 20 100
get_local_var()  # 900
print("LINE 22", var)  # LINE 22 100
add_var()  # 200
print("LINE 24", var)  # LINE 24 200
int_local_num()  # 300
print("LINE 26", var)  # LINE 26 200

# To Know the memory address
print(hex(id(int_local_num)))  # 0x104d97940
print((id(int_local_num)))  # 4376328512
print((type(int_local_num)))  # <class 'function'>

