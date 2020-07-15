"""
Program: manager.py.py
Author: Kelly Klein
Last date modified: 7/14/2020
This program will create a class called managers and include a display method to
    iterate through a list of employees under them
"""
import datetime

from derived_class import Person
from employee1 import Employee


class Manager(Person, Employee):
    def __init__(self, lname, fname, address, phone, start_date, salary, department='HR'):
        Person.__init__(self, lname, fname, address)
        Employee.__init__(self, lname, fname, address, phone, start_date, salary)
        self.last_name = lname
        # last_name: string
        self.first_name = fname
        # first_name: string
        self.address = address
        # address: string
        self.phone = phone
        # phone_number: string
        self.start_date = start_date
        # start_date: datetime
        self.salary = salary
        # salary: double
        self.department = department
        # department: string

    def __str__(self):
            str(self.first_name) + str(self.last_name) + str(self.address) + str(self.phone) + str(self.start_date) + str(self.salary) + str(department)

    def __repr__(self):
            repr(self.first_name + self.last_name + self.address + self.phone + self.start_date + self.salary + self.department)

    def display(self):
        return str(self.first_name) + str(self.last_name) + str(self.address) + str(self.phone) + str(self.start_date) + str(self.salary)


def display_employees(self):
    for i in list_of_dr:
        print(i)


if __name__ == '__main__':
    k_klein = Manager('Klein\n', 'Kelly ', '587 newb dr.\nCoralville, Iowa\n', '777-888-9999\n', str(datetime.datetime.now()), 40000)
    print(k_klein.display())
    direct_report1 = Employee('Joe\n', 'GI ', '909 patriot st.\nNowhere, USA\n', '444-555-6666\n', str(datetime.datetime.now()), 56000.00)
    #print(direct_report1)
    direct_report2 = Employee('Commander\n', 'Cobra ', '1313 bad guy ave.\nDesolation, Iowa\n', '333-111-8888\n', str(datetime.datetime.now()), 6000000.00)
    # print(direct_report2)
    list_of_dr = [direct_report1, direct_report2]
    display_employees(list_of_dr)
    del k_klein
    del direct_report2
    del direct_report1
    del list_of_dr
