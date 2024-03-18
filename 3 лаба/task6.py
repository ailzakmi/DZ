# 0 0 1 2 3 4 5 5 6 7
x = a = input("Введите число: ").split()
for i in range(len(a)-1): x += list('T' if (a[i] == a[i+1]) else 'F')
print(x.count('T') > 0)


# print(f"{1==1}") if x.count('T') > 0 else print(f"{1==0}")

# for i in a:print(f"{1==1}") if a.count(i) > 1 else print(f"{1==0}")

# for i in range(len(a)-1): x=1 if a.count(a[i]) > 1 else x=0
# print(f"{x==1}")

# for i in range(len(a)-1):
#     if a[i] == a[i+1]: print((b + 1).format(bool))
#     else: print(f"{0}".format(bool))

# a = [int(x) for x in input("Введите число: ")]
# print("yes") if a.count(0) == len(a) // 2 else print("no")