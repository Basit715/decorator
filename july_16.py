#function in python can be stored in data structures like list, hash table
def greet(name):
     return f"Welcome {name}"


lst = []
lst.append(greet)

# print(lst[0]("Basit"))


#function can be passed as an agrgument to another function

def shout(text):
     return text.upper()

def whisper(text):
     return text.lower()

def greet(func, name):
     greeting = func(f"Welcome {name}")
     print(greeting)
     
# greet(shout, "Basit") 
# greet(whisper, "Basit") 

#function can be returned from another function
def create_adder(x):
     def adder(y):
          return x + y
     
     return adder


add_15 = create_adder(15)
# print(add_15(10))


# ***************************decorators************************
def hello_decorator(func):
     def inner1():
          print(f"Hello, this is before function execution")
          
          func()
          
          print(f"This is after function execution")
          
     return inner1

def function_to_be_used():
     print("This is inside the function!!!!")
     
     
function_to_be_used = hello_decorator(function_to_be_used)

# function_to_be_used()




import time
import math

def calculate_time(func):
     def inner1(*args, **kwargs):
          begin = time.time()
          
          func(*args, **kwargs)
          
          end = time.time()
          
          print(f"Time taken by {func.__name__} is {end - begin}")
          
     return inner1



@calculate_time            # this line is exactly same as factorial = calculate_time(factorial)
def factorials(num):
     time.sleep(2)
     print(math.factorial(num))
     
     
factorials(5)