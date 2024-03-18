a = input("Введите число: ")
print()
ss = ""
if a.isdigit() != 1:
    print("Неверный ввод")

a = int(a)
b = a
c = a
while 1 == 1:
    if a == 2:
        ss += "0"
        break
    elif a == 1:
        ss += "1"
        break
    else:
        ss += str(a % 2)
        a = a // 2

print("Число в двоичной системе счисления: ", end="")
for i in range(len(ss)):
    print(ss[-i - 1], end="")
print()

ss = ""
while 1 == 1:
    if b == 0:
        break
    else:
        ss += str(b % 8)
        b = b // 8

print("Число в восьмеричной системе счисления: ", end="")
for i in range(len(ss)):
    print(ss[-i - 1], end="")
print()

ss = ""
while 1 == 1:
    if c == 0:
        break
    else:
        if 10 > int(c % 16):
            ss += str(c % 16)
        elif 10 == int(c % 16):
            ss += "A"
        elif 11 == int(c % 16):
            ss += "B"
        elif 12 == int(c % 16):
            ss += "C"
        elif 13 == int(c % 16):
            ss += "D"
        elif 14 == int(c % 16):
            ss += "E"
        elif 15 == int(c % 16):
            ss += "E"
        c = c // 16

print("Число в шестнадцатеричной системе счисления: ", end="")
for i in range(len(ss)):
    print(ss[-i - 1], end="")
print()