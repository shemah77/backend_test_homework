# Импорт модуля os из стандартной библиотеки
# для взаимодействия с операционной системой.
import os
# Считывание переменной окружения REMOTE_JUDGE, чтобы определить,
# локально выполняется код или на удалённом сервере.
LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

# Если код выполняется на локальном компьютере, то...
if LOCAL:
    # Класс, описывающий элементы связного списка:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item

        #def __str__(self):
         #   return f'[{self.value}]-›{self.next_item}'


def solution(node, idx:int):
    if idx == 0: return node.next_item
    current = node
    while idx > 1:
        current = current.next_item
        idx -= 1
        if current.next_item is None:
            #or current.next_item.next_item is None:
            current.next_item = node
            return node
    current.next_item = current.next_item.next_item
    #print(current)

    return node

    # Напишите код функции здесь.
    # ヽ(´▽`)/
    # Функция должна удалить из списка элемент с указанным индексом
    # и вернуть голову обновлённого списка.
    # if idx == 0: return node
    # current = node
    # i = 0
    # while current is not None:
    #     i = i + 1
    #     current  = current.next_item
    # if idx > i: return node
    #
    # head = node
    # current_node = head
    # count = 0
    # while current_node is not None:
    #
    #     if count == idx-1:
    #         #print(f'двигаюсь по нодам {current_node}')
    #         current_node.next_item = current_node.next_item.next_item
    #         #print(f'двигаюсь по нодам {current_node}')
    #         return head
    #     current_node = current_node.next_item
    #     count = count + 1







 # Тестирующая функция для проверки решения.
 # Не изменяйте её, она не требует вашего внимания.
def test():
    node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", None)
    node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
    node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
    node0 = Node("Задача 1: Фотосъёмка 360°", node1)

    new_head = solution(node0, 1)
    # Выражение, начинающееся с ключевого слова assert,
    # проверяет, что утверждение в выражении истинно.
    # Если утверждение ложно - в этом месте возникнет ошибка.
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
