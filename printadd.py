

def print_add():
  name = 'Jonathan'
  fullname = name + ' Adams'
  print(fullname) 

def traverse():
  lst = [1,2,3,4,5,6]
  for item in lst:
    print(item, end=' ')

def f_string():
  return f"\nI'm happy because I'm learning Git"

def all_in():
   print_add()
   traverse()
   print(f_string())

all_in()
