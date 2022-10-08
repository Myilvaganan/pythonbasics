"""
--------------------------------------OBJECT ORIENTED PROGRAMMING-----------------------------------------------------
TOPICS COVERED
1.  INTRO TO CLASS
2.  NOT EVERYTHING TO BE CLASS
3.  DATA AND BEHAVIOUR
4.  CREATE YOUR FIRST CLASS
5.  CLASS INSTANCES
6.  ADDING METHODS OR BEHAVIOUR TO YOUR PYTHON CLASS
7.  MAGIC METHODS
8.  INHERITANCE
9.  POLYMORPHISM
10. CLASS METHODS
11. STATIC METHODS
12. PROPERTY
13. GETTERS
14. SETTERS
------------------------------------------------------------------------------------------------------------------
"""

"""
--------------------------------------INTRO TO CLASS-----------------------------------------------------
IT IS USED WHEN NEED TO USE BOTH STRUCTURE AND BEHAVIOUR 

Inheritance:
------------

All species inherit a lot from their parents, may be they have same eyes as
their mother but different voice all together.
Python classes are no different, we can inherit from classes and make them share
common functionality. At the same time we can dynamically add other features and
functionality as well.

Polymorphism:
-------------
Suppose there are two children, one want's to speak in Marathi, other want's to
speak in Sanskrit. This is possible using polymorphism! It's just creating the same
methods but with different behavior.

------------------------------------------------------------------------------------------------------------------
"""


class ParentClass:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name}"

    def __repr__(self) -> str:
        return f"Class - Parent"

    def isAuthenticated(self) -> bool:
        return self.age >= 18


"""
print(ParentClass.isAuthenticated)  # <function ParentClass.isAuthenticated at 0x10e5a31f0>
print(ParentClass.__str__)  # <function ParentClass.__str__ at 0x10fd15940>
print(ParentClass.__repr__)  # <function ParentClass.__repr__ at 0x10fd158b0>
instance = ParentClass("Myilvaganan", 29)
print(instance.isAuthenticated())
instance2 = ParentClass("Ram", 17)
print(instance2.isAuthenticated())
"""


class Dob(ParentClass):
    def __init__(self, name: str, age: int, height: int, weight: int) -> None:
        super().__init__(name, age)
        self.height = height
        self.weight = weight

    def __str__(self) -> str:
        return f"Name: {self.name}, age: {self.weight}"

    def getBMI(self) -> str:
        bmi: float = self.weight / self.height * self.height
        return f"{self.name} BMI is: {bmi}"


a1 = ParentClass("Myilvaganan", 12)
a = a1.isAuthenticated()
print(a)

c1 = Dob("Myilvaganan", 17, 171, 89)
print(c1.getBMI())


class Animal:
    def __init__(self, name: str, age: int, num_legs: int) -> None:
        # Create & initialize instance variables
        self.name = name
        self.age = age
        self.num_legs = num_legs

    def __str__(self) -> str:
        return f"Name: {self.name}"

    def talk(self) -> None:
        """Makes the animal talk"""
        print(f"{self.name} can't talk yet!")


a1 = Animal("Robbin", 10, 4)
print(a1)


class Dog(Animal):
    def __init__(self, name: str, age: int, num_legs: int, breed: str) -> None:
        # Take the common features and pass to the parent(super) class
        super().__init__(name, age, num_legs)
        # Define custom instance variables
        self.breed = breed
        self.type = "Dog"

    def __str__(self) -> str:
        return f"{self.type}: {self.name}, Breed: {self.breed}"

    # We alter the talk method and make it say woff adding polymorphic behavior
    def talk(self) -> None:
        print(f"{self.name} says wofff...")

    def sniff(self, item: str) -> None:
        print(f"{self.name} is sniffing out {item}")


d1 = Dog("Whisky", age=5, num_legs=4, breed="Doberman")

print(d1)
d1.talk()
d1.sniff("ball")


class Cat(Animal):
    def __init__(self, name: str, age: int, num_legs: int, breed: str) -> None:
        super().__init__(name, age, num_legs)
        self.breed = breed
        self.type = "Cat"

    def __str__(self) -> str:
        return f"{self.type}: {self.name}, Breed: {self.breed}"

    def talk(self) -> None:
        print(f"{self.name} says meow...")


c1 = Cat("Jess", age=2, num_legs=4, breed="Persian Cat")

print(c1)
c1.talk()


class Dino(Animal):
    def __init__(self, name: str, age: int, num_legs: int, breed: str) -> None:
        super().__init__(name, age, num_legs)
        self.breed = breed
        self.type = "Dino"

    def __str__(self) -> str:
        return f"{self.type}: {self.name}, Breed: {self.breed}"

    def talk(self) -> None:
        print(f"{self.name} says urrghhhh...")

    def hunt(self) -> None:
        print(f"{self.name} is out for hunting...")


dino1 = Dino("Adam", age=8, num_legs=2, breed="T-Rex")

print(dino1)
dino1.talk()
dino1.hunt()

# -------------------------------------------------------------------------

print(isinstance(d1, Animal))
print(isinstance(d1, Dog))
print(isinstance(d1, Cat))

# -------------------------------------------------------------------------
