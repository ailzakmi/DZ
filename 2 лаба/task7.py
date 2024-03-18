# xyxxyx,x
a = input("Введите строку: ")
print()
l = 0
b = a.split(",")[1]

for i in range(len(a)):
    if a[i] == b:
        l += 1
    else:
        break
print(f"Количество символов расположенных в начале строки равно: {l}")