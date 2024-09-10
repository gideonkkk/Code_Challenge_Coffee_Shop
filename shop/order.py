from customer import Customer
from coffee import Coffee

class Order:
    all_orders =[]

    def __init__(self, customer, coffee, price):
        if isinstance(customer, Customer) and isinstance(coffee, Coffee):
            self._customer = customer
            self._coffee = coffee
        else:
            raise ValueError("Invalid customer or coffee instance.")
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
            Order.all_orders.append(self)
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")
            
    def customer(self):
        return self._customer
    def coffee(self):
        return self._coffee
    def price(self):
        return self._price