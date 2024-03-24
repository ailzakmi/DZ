class Node:
    """Вспомогательный класс для узлов списка"""
    def __init__(self, data):
        self.data = data # храним информацию
        self.pref = None # ссылка на предыдущий узел
class Stack:
    """Основной класс для стека"""
    def __init__(self):
        self.end = None # ссылка на конец стека
    def pop(self):
#         возвращение последнего элемента из списка с удалением его из списка
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
#         добавление элемента val в конец списка
        current_node = Node(val)
        current_node.pref = self.end
        self.end = current_node

    def print(self):
#         вывод на печать содержимого стека
        ch = self.end
        while ch:
            print(ch.data)
            ch = ch.pref

# Создать класс.
# Стек на структуре данных односвязный список.
# class Node:
#     """
#     Вспомогательный класс для узлов списка
#     """
#     def __init__(self, data):
#         self.data = data  # храним информацию
#         self.pref = None  # ссылка на предыдущий узел
#
# class Stack:
#     """
#     Основной класс для стека
#     """
#
#     def __init__(self):
#         self.end = None  # ссылка на конец стека
#
#     def pop(self):
#         """
#         возвращение последнего элемента из списка с удалением его из списка
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
#     def print(self):
#         """
#         вывод на печать содержимого стека
#         """
#         pass