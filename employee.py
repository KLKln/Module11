"""
Program: employee.py
Author: Kelly Klein
Last date modified: 7/11/2020
This program will create a class called employee and sub classes salaried_employee
    and hourly_employee
"""

import datetime


class Employee:
    def __init__(self, lname, fname, address, phone):

        """
        use reST style.
        :param last_name: employee's last name
        :param first_name: employee's first name
        :param address: employees address
        :param phone_number: employee's phone number

        :return:
        """
        self.last_name = lname
        #last_name: string
        self.first_name = fname
        #first_name: string
        self.address = address
        #address: string
        self.phone = phone
        #phone_number: string

    def display(self):
        """
        use reST style.
        :param last_name: employee's last name
        :param first_name: employee's first name
        :param address: employees address
        :param phone_number: employee's phone number

        :return:
        """
        print(self.first_name + ' ' + self.last_name)
        print(self.address)
        print(self.phone)

    def __str__(self):
        return(str(self.first_name + self.last_name, self.address, self.phone))

    def __repr__(self):
        return repr(self.first_name + self.last_name + self.address + self.phone)


class SalariedEmployee(Employee):
    def __init__(self, lname, fname, address, phone, start_date, salary):
        super().__init__(self, lname, fname, address)
        """
        use reST style.
        :param last_name: employee's last name
        :param first_name: employee's first name
        :param address: employees address
        :param phone: employee's phone number
        
        :return:
        """
        self.last_name = lname
        #last_name: string
        self.first_name = fname
        #first_name: string
        self.address = address
        #address: string
        self.phone = phone
        #phone_number: string
        self.start_date = start_date
        #start_date: dateTime
        self.salary = salary
        #salary: double

    def give_raise(self, new_salary):
        # updates salary
        self.salary = new_salary

    def display(self):
        # returns a string
        return str(self.first_name + ' ' + self.last_name + ' ' + self.address + ' ' + self.phone + ' ' + self.start_date + ' $' + str(self.salary) + '/yr')
        #print(self.first_name + ' ' + self.last_name)
        #print(self.address)
        #print(self.phone)
        #print(str(self.start_date))
        #print('$' + str(self.salary))


    def __str__(self):
        return str(self.first_name + self.last_name, self.address, self.phone, str(self.start_date), str(self.salary))

    def __repr__(self):
        return(repr(self.first_name + self.last_name + self.address + self.phone, str(self.start_date)), self.salary)





class HourlyEmployee(Employee):
    def __init__(self, lname, fname, address, phone, start_date, hourly_pay):
        super().__init__(self, lname, fname, address,)
        """
        use reST style.
        :param last_name: employee's last name
        :param first_name: employee's first name
        :param address: employees address
        :param phone_number: employee's phone number
        
        :return:
        """
        self.last_name = lname
        #last_name: string
        self.first_name = fname
        #first_name: string
        self.address = address
        #address: string
        self.phone = phone
        #phone_number: string
        self.start_date = start_date
        #start date: dateTime
        self.hourly_pay = hourly_pay
        #haourly pay: double

    def give_raise(self, new_hourly_pay):
        # updates salary
        self.hourly_pay = new_hourly_pay

    def display(self):
        # returns a string
        return str(self.first_name + ' ' + self.last_name + ' ' + self.address + ' ' + self.phone + ' ' + self.start_date + ' $' + str(self.hourly_pay) + '/hr')
        #print(self.first_name + ' ' + self.last_name)
        #print(self.address)
        #print(self.phone)
        #print(str(self.start_date))
        #print('$' + str(self.hourly_pay))

    def __str__(self):
        return str(self.first_name + self.last_name, self.address, self.phone, str(self.start_date), str(self.hourly_pay))

    def __repr__(self):
        return(repr(self.first_name + self.last_name + self.address + self.phone + self.start_date + self.hourly_pay))


if __name__ == '__main__':
    s_date = datetime.datetime.today()
    raistlin= SalariedEmployee('Majere', 'Raistlin', '900 Solace St.', '800-345-6789', str(s_date), 40000)
    print (raistlin.display())
    raistlin.give_raise(45000)
    print (raistlin.display())
    caramon = HourlyEmployee('Majere', 'Caramon', '1111 Krynn way', '800-398-4563', str(s_date), 10)
    print(caramon.display())
    caramon.give_raise(12)
    print(caramon.display())
