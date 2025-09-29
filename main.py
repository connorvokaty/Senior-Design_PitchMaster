# --------------------- ENTRY POINT TO THE PITCH MASTER SCRIPT ----------------------

def say_hello(name, age):
    print("Hello, " + name + "! Your age is " + age + ".")

my_name = input("What is your name? ")
my_age = input("How old are you? ")

say_hello(my_name, my_age)

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self, is_loud):
        if is_loud:
            print("bark!!")
        else:
            print("woof!")

    def get_older(self):
        self.age += 1

connors_dog = Dog("Freddy", "Golden Retriever", 4)

print(connors_dog.age)
connors_dog.bark(True)
connors_dog.get_older()

seths_dog = Dog("Seth", "Bobby", 8)

print(seths_dog.breed)
seths_dog.get_older()
print(seths_dog.age)