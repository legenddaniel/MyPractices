import random

feet_in_mile = 5280
meters_in_kilometer = 1000
big_cities = ["Beijing","Shanghai","Guangzhou","Shenzhen"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)

print()
class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    def honor(self):
        if self.gpa >= 3.5:
            return "Honored Graduate"
        else:
            return "No Honor"

print()
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

print()
class Chef:
    def chicken(self):
        print("This chef makes a chicken.")
    def salad(self):
        print("This chef makes a salad.")
    def special(self):
        print("This chef makes poutin.")

# from tools import Chef 由于在同一文件所以不需要引入
class ChineseChef(Chef):
    def rice(self):
        print("This chef makes rice.")

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")