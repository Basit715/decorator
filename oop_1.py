class Human:
     def __init__(self, first_name, last_name):
          self.first_name = first_name
          self.last_name = last_name
          
     def display(self):
          print(f"Your first name is {self.first_name} and last name is {self.last_name}")
          
          
          
class Student(Human):
     def __init__(self, first_name, last_name):
          super().__init__(first_name, last_name)
     
     def display(self):
          super().display()
          print("Student is derived from Human") 
          

stu = Student("Basit", "Pushoo") 
stu.display() 