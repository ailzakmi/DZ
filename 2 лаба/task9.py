# - ) (
# +7 (812) 134-12-324
a = input("Введите номер: ")
print()
ss = ""

for i in range(len(a)):
    if ("-" != a[i]) and (")" != a[i]) and ("(" != a[i]) and (" " != a[i]):
        ss += a[i]
print(f"Преобразованый номер: {ss}");