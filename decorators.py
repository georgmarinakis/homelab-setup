
# Function as object ########################################

def shout(text):
    return text.upper()

print(shout('reference to the function object'))

# reference to the function object
yell = shout

print(yell('reference to the function object'))

# Function as an argument ####################################

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

# passing function as an
def greet(func):
    greeting = func("""function as an argument""")
    print(greeting)

greet(shout)
greet(whisper)

# Returning function from another function

def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_15 = create_adder('inside function, ')
print(add_15('outside function'))

# Decorator########################
import time
import math

def calculate_time(func):
    def inner1(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in: ", func.__name__, end - begin)
    return inner1

@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))
factorial(10)