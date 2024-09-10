
class Coffee:
    all_coffees = []

    def __init__(self, name):
        if isinstance(name, str) and len(name) >=3:
            self._name = name
            Coffee.all_coffees.append(self)
        else:
            raise ValueError("Coffee name must be a string with at least 3 characters.")
    def name(self):
        return self._name
    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.coffee == self]
    def customers(self):
        from order import Order
        return list(set(order.customer for order in self.orders()))
    def num_orders(self):
        return len(self.orders())
    def average_price(self):
        orders = self.orders()
        if not orders: 
            return 0
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)
    
