# - ) (
# +7 (812) 134-12-324
a = input("Введите номер: ")
for i in range(len(a)):
    if ("-" != a[i]) and (")" != a[i]) and ("(" != a[i]) and (" " != a[i]): print(a[i], end='')