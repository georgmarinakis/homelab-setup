
# user-defined function
def f(x):
    return x * 2

print(f(9))

# lambda function
y = lambda x : x * 2

print(y(3))

# filter(function, iterable)
print("FILTER")

list1 = [1,2,3,4,5,6,7,8,9]
print(list1)

g = lambda x : x % 2 == 0

print(list(filter(g, list1)))

# Map(function, iterable)
print("MAP")

list2 = [2,3,4,5]
print(list2)

t = lambda x : pow(x, 2)

print(list(map(t, list2)))


# map new example
print("new MAP")
numbers = [1, 2, 3]

# def double(a):
#     return a * 2

double = lambda a : a * 2

result = map(double, numbers)
print(list(result))


# filter new example
numbers = [1,2,3]

# def isEven(n):
#     return n % 2 == 0

isEven = lambda a : a % 2 == 0

result = filter(isEven, numbers)

print(list(result))




