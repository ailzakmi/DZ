# 01011111101100111101
a = input("Введите число: ")
print()
l0 = 0
l1 = 0

for i in range(len(a)):
    if int(a[i]) == 0:
        l0 += 1
    else:
        l1 += 1

if l0 == l1:
    print("yes")
else:
    print("no")