from customer import Customer
from coffee import Coffee
from order import Order
 
if __name__ == "__main__":
     customer1 = Customer("Alpha")
     customer2 = Customer("Bravo")
     customer3 = Customer("Charlie")

     coffee1 = Coffee("Cappuccino")
     coffee2 = Coffee("Espresso")
     coffee3 = Coffee("Latte")

     order1 = customer1.create_order(coffee1, 5.5)
     order2 = customer2.create_order(coffee2, 6.0)
     order3 = customer3.create_order(coffee3, 3.0)

     print(f"{customer1.name}'s orders:", customer1.orders())
     print(f"{customer1.name}'s coffees:", customer1.coffees())

     print(f"{customer2.name}'s orders:", customer2.orders())
     print(f"{customer2.name}'s coffees:", customer2.coffees())

     print(f"{customer3.name}'s orders:", customer3.orders())
     print(f"{customer3.name}'s coffees:", customer3.coffees())

     print(f"{coffee1.name} orders:", coffee1.orders())          
     print(f"{coffee1.name} customers:", coffee1.customers())    
     print(f"{coffee1.name} num_orders:", coffee1.num_orders())     
     print(f"{coffee1.name} average price:", coffee1.average_price())

     print(f"{coffee2.name} orders:", coffee2.orders())          
     print(f"{coffee2.name} customers:", coffee2.customers())    
     print(f"{coffee2.name} num_orders:", coffee2.num_orders())     
     print(f"{coffee2.name} average price:", coffee2.average_price())

     print(f"{coffee3.name} orders:", coffee3.orders())          
     print(f"{coffee3.name} customers:", coffee3.customers())    
     print(f"{coffee3.name} num_orders:", coffee3.num_orders())     
     print(f"{coffee3.name} average price:", coffee3.average_price())

     print(order1.customer.name, "ordered", order1.coffee.name, "for", order1.price)   
     print(order2.customer.name, "ordered", order2.coffee.name, "for", order2.price)   
     print(order3.customer.name, "ordered", order3.coffee.name, "for", order3.price)    
 