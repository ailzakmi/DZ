def main():
    a = input("Введите число: ").split()
    x = int(a[0]) ** int(a[1])
    print("Ваше число: ", x)

if __name__ == "__main__":
    main()

# Создать класс.
# Очередь на структуре данных двусвязный список.
#
#
# class Node:
#     """
#     Вспомогательный класс для узлов списка
#     """
#     def __init__(self, data):
#         self.data = data  # храним информацию
#         self.nref = None  # ссылка на следующий узел
#         self.pref = None  # Ссылка на предыдущий узел
#
#
# class Queue:
#     """
#     Основной класс
#     """
#
#     def __init__(self):
#         self.start = None  # ссылка на начало очереди
#         self.end = None  # ссылка на конец очереди
#
#     def pop(self):
#         """
#         возвращаем элемент val из начала списка с удалением из списка
#         """
#         pass
#         return val
#
#     def push(self, val):
#         """
#         добавление элемента val в конец списка
#         """
#         pass
#
#     def insert(self, n, val):
#         """
#         вставить элемент val между элементами с номерами n-1 и n
#         """
#         pass
#
#     def print(self):
#         """
#         вывод на печать содержимого очереди
#         """
#         pass



class Node:
    """Вспомогательный класс для узлов списка"""
    def __init__(self, data):
        self.data = data # храним информацию
        self.nref = None # ссылка на следующий узел
        self.pref = None # Ссылка на предыдущий узел

class Queue:
    """Основной класс"""
    def __init__(self):
        self.start = None # ссылка на начало очереди
        self.end = None # ссылка на конец очереди

    def pop(self):
        val = self.start.data
        self.start = self.start.nref
        self.start.pref = None
        return val
    def push(self, val):
        current_node = Node(val)
        if self.start is None:
            self.start = current_node
            self.end = current_node
        else:
            current_node.pref = self.end
            self.end.nref = current_node
            self.end = current_node

    def insert(self, n, val):
        lst = []
        current_node = self.start

        while current_node:
            lst.append(current_node)
            current_node = current_node.nref
        new_node = Node(val)
        new_node.pref = lst[n-1]
        new_node.nref = lst[n]
        lst[n-1].nref = new_node
        lst[n].pref = new_node

    def print(self):
        ch = self.end
        while ch:
            print(ch.data)
            ch = ch.pref
queue = Queue()
for i in range(5):
    queue.push(i)
queue.print()
queue.insert(2,99)

print('______')
queue.print()