# Imports here

from motor_control import *

# --------------------- ENTRY POINT TO THE PITCH MASTER SCRIPT ----------------------

# Strictly using console commands

selected_waveform, operating_speed, ramp_time = command_speed()

while True:
    command = input("\nType the command you would like to execute: ")
    match command:
        case "help":
            print('''Here are a list of the commands: 

command = commands the motor how to operate            
start = runs the motor start up sequence
stop = runs the motor stop sequence
exit = exits the program''')
        case "command":
            command_speed()
        case "start":
            start_sequence(operating_speed, ramp_time)
        case "exit":
            break








# def say_hello(name, age):
#     print("Hello, " + name + "! Your age is " + age + ".")
#
# my_name = input("What is your name? ")
# my_age = input("How old are you? ")
#
# say_hello(my_name, my_age)
#
# class Dog:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
#
#     def bark(self, is_loud):
#         if is_loud:
#             print("bark!!")
#         else:
#             print("woof!")
#
#     def get_older(self):
#         self.age += 1
#
# connors_dog = Dog("Freddy", "Golden Retriever", 4)
#
# print(connors_dog.age)
# connors_dog.bark(True)
# connors_dog.get_older()
#
# seths_dog = Dog("Seth", "Bobby", 8)
#
# print(seths_dog.breed)
# seths_dog.get_older()
# print(seths_dog.age)