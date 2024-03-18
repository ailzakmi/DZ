# кот гири док
a = input("Введите строку: ")
print()

b1 = a.split()[0]
b2 = a.split()[1]
b3 = a.split()[2]

b = b1[len(b1)-1:len(b1):]
b += b2[len(b2)-1:len(b2):]
b += b3[len(b3)-1:len(b3):]
print(f"Новая строка: {b}")