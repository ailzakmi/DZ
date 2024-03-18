# www.google.com
a = input("Введите имя домена: ")
for i in range(len(a.split("."))):
    print(a.split(".")[-i - 1])