#1.  The `Person` class has a constructor that takes `name` and `age` as arguments and assigns them to the object's attributes. The `introduce` method is then invoked on the object to introduce the person.

# class Person:
#      def __init__(self, n, a):
#           self.name = n
#           self.age = a
          
#      def introduce(self):
#           print(f"Hello my name is {self.name} and my age is {self.age}")
          
          
# person1 = Person("Basit Pushoo", 26)

# person1.introduce()  


# 2.  the `Car` class has a constructor that takes `brand` and `model` as arguments and assigns them to the object's attributes. The `display_info` method is then invoked on the object to display the car's brand and model.

# class Car:
#      def __init__(self, br, mo):
#           self.brand = br
#           self.model = mo
          
#      def display(self):
#           print(f"My car is {self.brand} and model is {self.model}")
          

# car1 = Car("Hyundai", "Nexon")
# car1.display() 

# #. the `BankAccount` class has a constructor that takes `account_number` and `balance` as arguments and assigns them to the object's attributes. The `display_balance` method is then invoked on the object to display the account number and balance.

class BankAccount:
     def __init__(self, an, bal):
          self.account_number = an
          self.balance = bal
          
     def display_balance(self):
          print(f"My account number is {self.account_number} and the balance is {self.balance}")
          

customer1 = BankAccount("874356554", 100)
customer1.display_balance() 
          
          
          