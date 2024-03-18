# полиндром
# поллоп
# этопэто
def main():
    a = input("Введите слово: ")
    # a = "полиндром"
    # a = "поллоп"
    # a = "этоээпэто"
    # a = "этоээпэтор"
    # print(a)

    li = []
    for i in a:
        j = a.count(i)
        if j != 1:
            if i not in li:
                li.append(i)
                li.append(j)
        else:
            if i not in li:
                li.append(i)
                li.append(1)
    # print(*li, sep='')

    # li += '`'
    b = ""
    x = ""
    # while 1==1:

    for i in range(len(li)):
        # print(i, end="")
        # if li[i]=='`':break
        if (i%2)==0: b += li[i]
        if (i%2)==1: x += str(li[i])
        # print(i, end="")

    # print("----------------------------")
    # print(b)
    # print(x)
    # print("----------------------------")

    li.clear()
    for i in range(len(b)):
        # print(1, end="")
        # nun = int(x[r]) // 2
        # print(nun)
        for j in range(int(x[i])//2):
            # print(b[r], end="")
            li.append(b[i])

    for i in range(len(b)):
        # print(1, end="")
        # nun = int(x[r]) // 2
        # print(nun)
        if int(x[i]) == 1:
            # print(b[r], end="")
            li.append(b[i])

    for i in range(len(b)):
        # print(1, end="")
        # nun = int(x[r]) // 2
        # print(nun)
        for j in range(int(x[-i-1])//2):
            # print(b[::-1][r], end="")
            li.append(b[::-1][i])

    # print(*li)

    b = ""

    for i in range(len(li)):
        if (li[i] != " "): b += str(li[i])

    # print(b)
    # if a == a[::-1]:
    #     print("Ваш полиндром: ", a)
    # el
    if b == b[::-1]:
        print("Ваш полиндром: ", b)
    else:
        print("Это не полиндром")

if __name__ == "__main__":
    main()

# На вход подается строка.
# Напишите функцию для реализации: если из слова можно составить палиндром,
# то составить его и вывести на экран.