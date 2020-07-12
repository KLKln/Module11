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
        return str(self.last_name) + ", " + str(self.first_name) + '\n' + self.address.display()


class Address:
    """Address class for US addresses"""
    def __init__(self, st_number, st_name, st_type, city, state, zip, apt_num=''):
        self.street_number = st_number
        self.street_name = st_name
        self.street_type = st_type
        self.apartment_number = apt_num
        self.city = city
        self.state = state
        self.zip_code = zip

    def __str__(self):
        return 'address: ', self.street_number, self.street_name, self.street_type, self.apartment_number, self.city, self.state. self.zip_code

    def display(self):
        return(self.street_number + ' ' + self.street_name + ' ' + self.street_type + ' ' + self.apartment_number
               + '\n' + self.city + ', ' + self.state + ' ' + self.zip_code)


if __name__ == '__main__':

    addy = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111')
    person1 = Person('Hammer', 'Martin', addy)
    print(person1.display())
# apartemnt number is at the end. Why?
    addy = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111', '16B')
    person2 = Person('Hammer', 'Martin', addy)
    print(person2.display())
    del(addy)
    del(person1, person2)
