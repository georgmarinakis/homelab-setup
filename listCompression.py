
# List Comprehension - shorter syntax

fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# solution 

fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = [x for z in fruits if "a" in z]
print(newlist)

#########################################################

numbers = [1,2,3,4,5]

# Comprehension
numbers_power = [n**2 for n in numbers]
print(numbers_power)

# classic for
num_power = []
for n in numbers:
    num_power.append(n**2)

print(num_power)

# lambda
numbers_p = list(map(lambda n : n**2, numbers))
print(numbers_p)


