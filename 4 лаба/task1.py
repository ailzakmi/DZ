# 10 10 10 10 10
# 1 2 3 3 2 1 4 56 7 98 10 22 10 45
# 1 2 3 4 5 6 7 8 9 10
def main():
    a = input("Введите число: ").split()
    x = 0
    for i in a: x += 1 if a.count(i) > 1 else 0
    if (x == len(a)):
        print("Все числа равны")
    elif (x == 0):
        print("Все числа разные")
    elif (x > 0):
        print("Есть равные и неравные числа")
    else:
        print("Вы вообще числа ввели?")

if __name__ == "__main__":
    main()

# a = [int(x) for x in input("Введите число: ")]
# print("yes") if a.count(0) == len(a) // 2 else print("no")

# На вход подается список чисел через пробел.
# Напишите функцию выводящую сообщение для списка чисел:
# 1) Все числа равны
# 2) Все числа разные
# 3) Есть равные и неравные числа
