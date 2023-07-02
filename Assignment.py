# 1.  The `Person` class has a constructor that takes `name` and `age` as arguments and assigns them to the object's attributes. The `introduce` method is then invoked on the object to introduce the person.

# class Person:
#      def __init__(self,n, a):
#           self.name = n
#           self.age = a
#      def display(self):
#           print(f"Hello my name is {self.name} and my age is {self.age}")
          

# person1 = Person("Basit", 26)
# person1.display() 


# 2. the `Car` class has a constructor that takes `brand` and `model` as arguments and assigns them to the object's attributes. The `display_info` method is then invoked on the object to display the car's brand and model.

# class Car:
#      def __init__(self, br, mo): 
#           self.brand = br
#           self.model = mo
          
#      def display(self):
#           print(f"My car {self.brand} {self.model} is making a roaring sound")
          
# car1 = Car("hyundai", "nexon")
# car1.display() 

# 3.the `BankAccount` class has a constructor that takes `account_number` and `balance` as arguments and assigns them to the object's attributes. The `display_balance` method is then invoked on the object to display the account number and balance.

# class BankAccount:
#      def __init__(self, an, bal):
#           self.account_number = an
#           self.balance = bal
          
#      def display(self):
#           print(f"Your account with account number as {self.account_number} has a balance of {self.balance}")
          

# cus1 = BankAccount("1234567", 200)
# cus1.display() 
          
# 4. the `MobilePhone` class has a constructor that takes `brand` and `model` as arguments and assigns them to the object's attributes. The `make_call` method is then invoked on the object to make a call with the phone.

# class MobilePhone:
#      def __init__(self, br, mo):
#           self.brand = br
#           self.model = mo
          
#      def display(self):
#           print(f"i have {self.brand} {self.model}")
          
# obj = MobilePhone("iphone", "12 pro max") 
# obj.display() 

#5. the `Book` class has a constructor that takes `title` and `author` as arguments and assigns them to the object's attributes. The `display_info` method is then invoked on the object to display the book's title and author.

# class Book:
#      def __init__(self, t, a):
#           self.title = t
#           self.author = a
#      def display(self):
#           print(f"The book titles {self.title} and its written by {self.author}")
          
# b1 = Book("self love", "Anand vihar")
# b1.display()

# 6. Vehicles: Create a base class called Vehicle with attributes such as make, model, and year. Implement two subclasses Car and Motorcycle that inherit from Vehicle. Add additional methods to the subclasses, such as start_engine() and stop_engine(), and handle any specific behavior or rules for each vehicle type.

# class Vehicle:
#      def __init__(self, model, year):
#           self.model = model
#           self.year = year
          
     
# class Car(Vehicle):
#      def start_engine(self):
#           print(f"{self.model} has started its engine")
#      def stop_engine(self):
#           print(f"{self.model} has stopped its engine")
          
# class MotorCycle(Vehicle):
#      def start_engine(self):
#           print(f"{self.model} has started its engine")
#      def stop_engine(self):
#           print(f"{self.model} has stopped its engine")
          

# c1 = Car("i20", 2011)
# c1.start_engine()
# c1.stop_engine()


# m1 = MotorCycle("Himalyan", 2022)
# m1.start_engine()
# m1.stop_engine() 

# 7. Animals: Create a base class called Animal with methods such as eat() and sleep(). Implement two subclasses Dog and Cat that inherit from Animal. Add additional methods to the subclasses, such as bark() for dogs and meow() for cats, and handle any specific behavior or rules for each animal type.

# class Animal:
#      def __init__(self, name):
#           self.name = name
          
#      def eat(self):
#           print(f"{self.name} is eating")
#      def sleep(self):
#           print(f"{self.name} is sleeping")
          
# class Dog(Animal):
#      def bark(self):
#           print(f"{self.name} is barking")
          
# class Cat(Animal):
#      def meow(self):
#           print(f"{self.name} is making meow sounds")
          
          
# d1 = Dog("tommy")
# d1.bark()


# c1 = Cat("rinu")
# c1.eat()


#8. Library Catalog: Create a base class called LibraryItem with attributes such as title, author, and publication_year. Implement two subclasses Book and Magazine that inherit from LibraryItem. Add additional methods to the subclasses, such as checkout() and return_item(), and handle any specific behavior or rules for each item type.
# class LibraryItem:
#      def __init__(self, title, author, publication_year):
#           self.title = title
#           self.author = author
#           self.publication_year = publication_year
          
          
# class Book(LibraryItem):
#      def checkout(self):
#           print(f"You have checked out with a book titled {self.title}")
#      def Return(self):
#           print(f"You have returned the book titled {self.title}")


# class Magazine(LibraryItem):
#      def checkout(self):
#           return f"You have checked out with book titled {self.title}"
     
     
#      def Return(self):
#           return f"You have returned the book with title {self.title}"
     
     

# book_name = input("Enter the name of book you need: ")
# author_name = input("Enter the name of author: ")
# pub_year = int(input("Enter the publication_year: "))

# b1 = Book(book_name, author_name, pub_year)

# b1.checkout()
# b1.Return()

# 9. Employees and Departments: Create a base class called Employee with attributes such as name, salary, and department. Implement two subclasses Manager and Staff that inherit from Employee. Add additional methods to the subclasses, such as assign_task() for managers and attend_meeting() for staff members. Create a separate class called Department that contains a list of employees and methods to add or remove employees from the department.

# class Employee:
#      def __init__(self, name, salary, department):
#           self.name = name
#           self.salary = salary
#           self.department = department
          
# class Manager(Employee):
#      def assign_task(self):
#           print(f"A new project setup is required within a day or two")
          
# class Staff(Employee):
#      def attend_meeting(self):
#           print(f"All the staff members are directed to attend the meeting regarding a new project today")
          

# lst = []

# class Department:
#      def add_employee(self): 
#           name = input("Enter the name of new employee: ")
#           lst.append(name)
#           print(f"{name} has been added successfully ")
          
#      def remove_employee(self): 
#           name = input("Enter the name of employee to be removed: ")
#           lst.remove(name)
#           print(f"{name} has been removed successfully ")
          
#      def display(self):
#           for i in lst: 
#                print(i)
               

# for i in range(0,3):
#      d1 = Department()
#      d1.add_employee()
     
# d1.display() 

# is_remove = input("Do you need to remove any employye if yes: type True or False" )

# if is_remove:
#      d1.remove_employee()
# else:
#      print("No updation needed")
     
# d1.display()    
 

#10. Bank Transactions: Create a base class called BankAccount with attributes such as account_number and balance. Implement subclasses for different types of accounts such as CheckingAccount and SavingsAccount that inherit from BankAccount. Add additional methods to the subclasses, such as withdraw() and deposit(), and handle any specific behavior or rules for each account type.

# class BankAccount:
#      def __init__(self, account_number, balance):
#           self.account_number = account_number
#           self.balance = balance
          
#      def checkBal(self):
#           print(f"Your balance is {self.balance}")
          
# class CheckingAccount(BankAccount):
#      def deposit(self, amount):
#           self.balance+=amount
     
     
#      def withdraw(self, amt):
#           self.balance-=amt
          
          
# class SavingsAccount(BankAccount):
#      def deposit(self, amount):
#           self.balance+=amount 
      
     
#      def withdraw(self, amt):
#           self.balance-=amt
          
          
# acc1 = SavingsAccount("12345678", 100)
# acc1.deposit(3000)
# acc1.checkBal()
# acc1.withdraw(2700)
# acc1.checkBal() 



     
          
          


      
          

     
          

          
         
          
          
          


