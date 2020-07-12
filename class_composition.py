"""
Program: class_composition.py
Author: Kelly Klein
Last date modified: 7/8/2020
This program will take input from main and output a student and person class
    displaying information about student
"""
from datetime import datetime


class Person:
    """Person class"""

    def __init__(self, lname, fname, addy=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def __str__(self):
        return self.last_name, self.first_name, self.address

    def __repr__(self):
        return self.last_name, self.first_name

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name)


class Student:
    def __init__(self, major, gpa, start_date=str(datetime), person=Person('','')):
        self.major = major
        self.gpa = gpa
        self.start_date = start_date
        self.person = person

    def change_major(self, new_major):
        self.major = new_major

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

    def __str__(self):
        return self.major, self.start_date, self.gpa, str(self.person.display)

    def display(self):
        return str(self.major, self.start_date, self.gpa)


# def display(self):
# return str(self.last_name) + ", " + str(self.first_name) + '\n' + self.address.display()


if __name__ == '__main__':
    person_kelly = Person('Klein', 'Kelly')
    student_kelly = Student('CIS',  4.0, str(datetime(2019, 2, 3)), person_kelly)
    student_kelly.display()
    student_kelly.change_major('Being Awesome!')
    student_kelly.display()
    student_kelly.update_gpa(3.0)
    student_kelly.display()
    del(person_kelly, student_kelly)
