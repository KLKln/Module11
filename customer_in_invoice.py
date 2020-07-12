"""
Program: customer_in_invoice.py
Author: Kelly Klein
Last date modified: 7/8/2020
This program will take input from main and output a series of strings in the
    form of an invoice
"""


class Customer:
    def __init__(self, customer_id, lname, fname, phone, address):
        """
use reST style.
    :param customer_id: unique int assigned to identify customer
    :param last_name: customer's last name
    :param first_name: customer's first name
    :param phone: customer's phone number
    :param address: customer's address
    :return:
"""
        self.cid = customer_id
        # customer_id: int: required
        self.last_name = lname
        # last_name: string: required
        self.first_name = fname
        # first_name: string: required
        self.phone = phone
        # phone_number: string: required
        self.address = address
        # address: string: required

    def __str__(self):
        return str(self.cid + self.last_name + self.first_name, self.phone, self.address)

    def __repr__(self):
        return repr(self.cid + self.last_name + self.first_name + self.phone + self.address)


class Invoice:
    def __init__(self, invoice_id, custy = Customer, items_with_price={}):
        """
use reST style.
    :param invoice_id: unique int assigned to identify an invoice
    :param customer_id: unique int assigned to identify customer
    :param last_name: customer's last name
    :param first_name: customer's first name
    :param address: customer's address
    :param phone_number: customer's phone number
    :return:
"""


        self.invoice_id = invoice_id
        # invoice_id: int: required
        self.customer = custy
        self.items_with_price = items_with_price
        # items_with_price: dictionary, optional
        # since optional, how do we default to a 'blank' dictionary

    def create_invoice(self):
        """
    use reST style.

        :return:

"""

        print(custy)
        subtotal = 0
        # items_with_price = {}
        # loop over each k, v pair in items_with_price
        # print str(key) + '.....' + str(value)
        # subtotal assigned to itself + value
        for k, v in self.items_with_price.items():
            print(k, ':', v)
            subtotal += v
        # at end of loop we have the sum of all values
        # tax = 6%
        tax = .06
        # tax_owed = subtotal * tax
        tax_owed = subtotal * tax
        # total is tax_owed + subtotal
        total = subtotal + tax_owed
        # print our tax ........108.00
        print('Tax Owed.........' + '$', tax_owed)
        # print our total ........ 1907.98
        print('Total..........' + '$', total)

    def add_item(self, item_price_dict):
        """
    use reST style.
        :param item_price_dict: passes in values from main, updates dict items_with_price
"""
        for key, value in item_price_dict.items():
            self.items_with_price[key] = value

    # invoice_id, customer_id, lname, fname,  phone, address
    def __str__(self):
        return self.invoice_id, self.customer

    def __repr__(self):
        return self.invoice_id, self.customer


if __name__ == '__main__':
    # Driver
    captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
    invoice = Invoice(1, captain_mal)
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
