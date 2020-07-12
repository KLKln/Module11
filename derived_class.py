"""
Program: derived_class.py
Author: Kelly Klein
Last date modified: 7/11/2020
This program will take input from main and output a student class derived from
    a person class
"""
class Person:
    """Person class"""

    def __init__(self, lname, fname, addy=''):
        self._last_name = lname
        self._first_name = fname
        self._address = addy

    def display(self):
        return str(self._last_name + ",", self._first_name + ":" + self._address)


class Student(Person):
    """Student subclass"""

    def __init__(self, lname, fname, major='Computer Science', gpa='0.0', student_id=900111111):
        super().__init__(self, lname, fname)
        self.__student_id = student_id
        self.__last_name = lname
        self.__first_name = fname
        self.__major = major
        self.__gpa = gpa

    def display(self):
        #return """%s, %s: (%s) %s, %s"""%(self.__last_name, self.__first_name, self.__student_id, self.__major, self.__gpa)
        #return str(self.__last_name), str(self.__first_name)+ ':' + '(' + str(self.__student_id)  + ')' + str(self.__major), str(self.__gpa)
        return str(self.__last_name, self.__first_name, self.__student_id, self.__major, self.__gpa)


if __name__ == '__main__':
    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', '4.0')
    print(my_student.display())
    del my_student
