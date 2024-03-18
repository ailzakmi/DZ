a = input("Введите три числа: ")
print()

b = a.find(" ", 0, len(a))
ch1 = int(a[:b])
print(ch1, end=" ")
a = a[b+1:]
b = a.find(" ", 0, len(a))
ch2 = int(a[:b])
print(ch2, end=" ")
a = a[b+1:]
ch3 = int(a)
print(ch3)
print()
print("Среднее число: ", end="")
if ch1 < ch2:
    if ch2 < ch3:
        print(ch2)
    elif ch1 < ch3:
        print(ch3)
    else:print(ch1)
elif ch1 < ch3:
    print(ch1)
elif ch2 < ch3:
    print(ch3)
else:print(ch2)