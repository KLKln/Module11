"""
Program: employee.py
Author: Kelly Klein
Last date modified: 7/11/2020
This program will create a class called managers and include a display method to
    iterate through a list of employees under them
"""
import datetime

from derived_class import Person
from employee1 import Employee


class Manager(Person, Employee):
    def __init__(self, lname, fname, address, phone, start_date, salary, department):
        super().__init__(self, lname, fname)
        super().__init__(self, address, phone, start_date, salary)
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

    def display(self):
        return str(self.first_name + self.last_name + self.address + self.phone, self.start_date + self.start_date, self.salary)

        pass


if __name__ == '__main__':
    k_klein = Manager('Klein', 'Kelly', '587 newb dr.\n Coralville, Iowa', '777-888-9999', str(datetime.datetime.now()),
                      40000, 'Grocery')
    print(k_klein.display())
    direct_report1 = Employee('Klein', 'Kelly', '000 blank st.\n Coralville, Iowa', '444-555-6666', True,
                              str(datetime.datetime.now()), 40000.00)
    # print(direct_report1)
    direct_report2 = Employee('Klein', 'Kelly', '000 blank st.\n Coralville, Iowa', '444-555-6666', True,
                              str(datetime.datetime.now()), 40000.00)
    # print(direct_report2)
    list_of_dr = [direct_report1, direct_report2]
