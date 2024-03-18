def main():
    a = input("Введите число: ").split()
    b = int(a[1])
    a = int(a[0])
    # a = int(input())
    # b = int(input())

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    print("НОД:", a + b)

if __name__ == "__main__":
    main()

# На вход подается два числа через пробел: a, b.
# Напишите функцию для реализации рекурсивного алгоритма Евклида
# поиска наибольшего общего делителя.