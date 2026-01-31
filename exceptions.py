
# Exception

filename = 'D:/Python/test.txt'

try:
    file = open(filename, 'r', encoding = 'utf8')
    content = file.read()
    print(content)
finally:
    file.close()


# Exception with 'with'

with open(filename, 'r', encoding = 'utf8') as file:
    content = file.read()
    print("\n" + content)

