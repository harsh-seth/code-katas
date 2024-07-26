class Greeter:
    def __init__(self, name):
        self.name = name
    
    def sayHello(self):
        print(f"Hello {self.name}!")
    
    @staticmethod
    def sayGoodbye():
        print("Goodbye!")

    def __add__(self, other):
        return Greeter(f"{self.name} & {other.name}")
    
    @property
    def age(self):
        print("age was accessed!")
        return self.ageMirror
    
    @age.setter
    def age(self, val):
        print("age was 'set'!")
        self.ageMirror = val


# Object creation
greetPerson1 = Greeter("harsh")

# Attribute access
print(f"name: {greetPerson1.name}")
# Private members do not exist in Python

# Member function invocation
greetPerson1.sayHello()
greetPerson1.sayGoodbye() # Will not work as sayGoodbye is a static function
# Greeter.sayHello() # Will not work as sayHello needs an object reference
Greeter.sayHello(greetPerson1) # Analogous to a JS bind (?)
Greeter.sayGoodbye()

# New attribute
greetPerson1.alt = '10'
print(f"alt: {greetPerson1.alt}")
del greetPerson1.alt
# print(f"alt: {greetPerson1.alt}") # Will not work as alt was deleted

# Getter/Setter
greetPerson1.age = "20"
print(f"age: {greetPerson1.age}")

# Operator overloading
greetPerson2 = Greeter("yash")
greetComposite = greetPerson1 + greetPerson2
greetComposite.sayHello()

print("---")
