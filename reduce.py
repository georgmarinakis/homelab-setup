from functools import reduce

words = ['Python', 'Reduce','Function', 'Tutorial']

l = lambda x, y : x + ' ' + y

sentence = reduce(l, words)

print(sentence)

########################################################


numbers = [1,2,3,4,5]

product = 1

# for num in numbers:
#     product *= num

l = lambda x, y : x * y



print(reduce(l,numbers))