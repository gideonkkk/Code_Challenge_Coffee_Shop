class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)
    def name(self):
        return self._name
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <=15:
            self._name = new_name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")
    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.customer == self]
    def coffes(self):
        from order import Order
        return list(set(order.coffee for order in self.orders()))
    def create_order(self,coffee, price):
        from order import Order
        from coffee import Coffee
        if isinstance(coffee, Coffee):
            return Order(self, coffee, price)
        else:
            raise ValueError("Must provide a valide Coffee object.")
 