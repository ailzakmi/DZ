a = input("Введите число: ")
if a.isdigit() != 1:print("Неверный ввод")
else:print(f'Двоичное: {int(a):b} | Восьмеричное: {int(a):o} | Шестнадцатеричное: {int(a):x}')