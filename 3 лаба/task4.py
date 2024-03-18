# 01011111101100111101
# 01010101010101
a = [int(x) for x in input("Введите число: ")]
print("yes") if a.count(0) == len(a) // 2 else print("no")