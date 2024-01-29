
def input_data():
    '''input data from user'''
    qty_container: int = int(input())
    containers_array: list = [int(x) for x in input().split()]
    instruction_qty: int = int(input())
    instruction_array_template: list = [int(x) for x in input().split()]

    return qty_container, containers_array, instruction_qty, instruction_array_template

def insertion_sort(arr: list, element_sort:int):
    # Проходим по всем элементам массива, начиная со второго.
    for i in range(1, len(arr)):
        # Сохраняем текущий элемент в переменную current.
        current = arr[i]
        # Сохраняем индекс предыдущего элемента
        # в переменную prev (от previous - предыдущий).
        prev = i - 1
        # Сравниваем current с предыдущим элементом
        # и двигаем предыдущий элемент на одну позицию вправо,
        # пока он больше current и не достигнуто начало массива.
        while prev >= 0 and arr[prev] > current:
            arr[prev + 1] = arr[prev]
            prev -= 1
        # Вставляем current в отсортированную часть массива на нужное место.
        arr[prev + 1] = current
        print(f'Шаг {i}, отсортировано элементов: {i + 1}, {arr}')

def intersection_list(list1, list2): # находит разницу между массивами 1 и 2
   list3 = [value for value in list1 if not value in list2]
   return list3

def sort_by_temp(qty_container: int,  containers_array: list,
                 instruction_qty:int, instruction_array_template:list):
    '''sort containers by template'''
    final_arr: list = []
    final_arr_add: list = intersection_list(containers_array, instruction_array_template)
    final_arr_add.sort()



    # сортировка по шаблону основного массива
    for i in instruction_array_template:
        element_sort = i
        for j in containers_array:
            if j == element_sort:
                final_arr.append(j)
     # если что-то осталось - контейнеры которых нет в шаблоне
    if len(final_arr) < qty_container:
        final_arr += final_arr_add

    return final_arr



if __name__ == '__main__':
    (qty_container, containers_array,
     instruction_qty, instruction_array_template) = input_data() # ввод данных
    result = sort_by_temp(qty_container, containers_array,
                 instruction_qty, instruction_array_template) # создание массива
    #print (result)
    print(' '.join(map(str, result)))

