
# def bubble_sort(data):
#     last_index = len(data) - 1
#     while last_index >= 0:
#         swapped = False
#         for item_index in range(last_index):
#             if data[item_index] > data[item_index+1]:
#                 data[item_index], data[item_index+1] = (
#                     data[item_index +1], data[item_index]
#                 )
#                 swapped = True
#         if swapped == True:
#             last_index -= 1
#         else: return data
#
#     # Напишите здесь код сортировки.
#     # return data

def bubble_sort(data):
    # Создаём внешний цикл for, указываем диапазон range.
    # Первый аргумент в range - начало диапазона: len(data) - 1.
    # Второй аргумент - конец диапазона (не включается в диапазон): 0.
    # Третий аргумент - шаг для получения следующего значения диапазона: -1.
    # На каждой итерации переменная last_index будет уменьшаться на 1.
    for last_index in range(len(data) - 1, 0, -1):
        # На этом проходе перестановок ещё не было:
        swapped = False
        # Вложенный цикл будет перебирать значения от 0 до last_index
        # (не включая last_index).
        for item_index in range(last_index):
            # Сравниваем значения текущего и следующего элементов списка.
            if data[item_index] > data [item_index + 1]:
                # Если значения надо поменять местами - меняем.
                # Круглые скобки стоят, чтобы перенести длинную строку.
                data[item_index], data[item_index + 1] = (
                    data[item_index + 1], data[item_index]
                )
                # Выставляем флаг "выполнена перестановка".
                swapped = True
        # После окончания внутреннего цикла проверяем значение флага.
        # Если перестановок не было...
        if not swapped:
            # ...то выходим из внешнего цикла.
            break
    # Возвращаем отсортированный список.
    return data

def find_element(sorted_numbers, element):
    """Находит индекс element в отсортированном списке sorted_numbers."""
    # Левая граница (левый индекс) рассматриваемого набора элементов.
    # В начале работы она равна индексу первого элемента в списке - нулю.
    left = 0
    # Правая граница (правый индекс) рассматриваемого набора элементов.
    # В начале работы она равна индексу последнего элемента в списке.
    right = len(sorted_numbers) - 1
    # Пока левая граница меньше правой или равна ей:
    while left <= right:
        # Находим в наборе элементов индекс среднего элемента.
        mid = (left + right) // 2
        # Если элемент с этим индексом равен искомому, возвращаем его индекс.
        if sorted_numbers[mid] == element:
            return mid
        # Если средний элемент меньше искомого...
        if sorted_numbers[mid] < element:
            # ...то изменяем левую границу поиска:
            left = mid + 1
        # Если средний элемент больше искомого...
        else:
            # ...то изменяем правую границу поиска:
            right = mid - 1
    # Если левая граница оказалась больше правой,
    # значит, элемент не найден. Возвращаем None.
    return left






def main():
    concetration_list = [int(x) for x in input().split()]  # Считали первую строку ввода.
    target = int(input()) # Считали вторую строку ввода.

    # если список одинаковый
    if len (concetration_list) == concetration_list.count(concetration_list[0]):
        # если список одинаковый
        if target > concetration_list[0]:
            print(len(concetration_list)) # вставуляем элемент
            # в конец если массив состоит из одинаковых элементов
        else: print(0)

        # если список одинаковый печаеем индекс первого элемента
    else:
            result  = find_element(concetration_list,target)
            print(result)


    # Обязательно печатаем результат, иначе Яндекс Контест не увидит решение!
    # print(' '.join(result))


if __name__ == '__main__':
    # Решение оформлено в функцию, эту функцию надо обязательно вызвать:
    # Яндекс Контест не сможет вызвать её сам.
    main()

