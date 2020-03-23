from functools import total_ordering

#Decorator, this allows us to take existing code and augment it with additional behaviour
@total_ordering
class Customer:
  customer_id = 0
  
  #dunder method, the class initializes the object, it will expect two arguments only!
  def __init__(self, name:str, car:str) -> None:
    self.name = name
    self.car = car
    Customer.customer_id += 1
    self.id = Customer.customer_id
    self._payments = []
  
  def display_details(self):
    print('Name: %s\nID: %i\nCar: %s\n' %(self.name, self.id, self.car))

  def update_car(self, car:str) -> None:
    self.car = car

  #we are defining __repr__ as representation, this way our object will behave like defined if printed
  def __repr__(self):
    return str('Name: %s\nID: %i\nCar: %s\n' %(self.name, self.id, self.car))

  def add_payment(self, amount):
    if not isinstance(amount, int):
      raise ValueError('The value for amount needs to be int')
    self._payments.append(amount)

  def __len__(self):
    return len(self._payments)
  
  #Because of the decorator, we only need to declare these two dander units.
  def __eq__(self, other):
    return sum(self._payments) == sum(other._payments)

  def __lt__(self, other):
    return sum(self._payments) < sum(other._payments)


customer1 = Customer('Klara', 'Audi A4')
customer1.display_details()

customer2 = Customer('Eric', 'Mazda 6')
customer2.display_details()

customer1.update_car('Volkswagen Golf')
customer1.display_details()

print(customer1)

customer1.add_payment(30)
customer1.add_payment(24)
customer1.add_payment(33)
customer1.add_payment(37)

print(len(customer1))

customer2.add_payment(36)
customer2.add_payment(35)
customer2.add_payment(35)

print(len(customer2))

print(customer1 > customer2)

customer2.add_payment(41)
print(customer1 > customer2)
