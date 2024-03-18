# www.google.com
a = input("Введите имя домена: ")
print()

# print(a.split("."))
# print(len(a.split(".")))

for i in range(len(a.split("."))):
    print(a.split(".")[-i - 1])
print()