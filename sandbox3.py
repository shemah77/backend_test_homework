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
# data = [1, 2, 3, 2, 5, 1, 7, 99, 9, 10]
#
# data4 = data[2:]
#
#
# data3 = sorted(data)
# data2 = bubble_sort(data)
# print (data3 == data2)


def main():
    mountain_list = [int(x) for x in input().split()]  # Считали первую строку ввода.
    # target = int(input()) # Считали вторую строку ввода.
    peak = max(mountain_list)
    peak_index = mountain_list.index(peak)
    list_up = mountain_list[:peak_index + 1]
    list_down = mountain_list[peak_index:]
    # print (list_up)
    # print (list_down)
    list_down_sorted  =  sorted(list_down, reverse = True)
    # print (list_down_sorted)
    Mount_up = False
    Mount_down = False
    Mount_flat = False
    Mount_equal = False

    Mount_check = False


    if list_up == sorted(list_up):
        Mount_up = True
        # print(f' check UP {Mount_up}')
        if list_down == list_down_sorted:
            Mount_down = True
            # print (f'Check DOWN{Mount_down}')

    # если список одинаковый
    if len (mountain_list) == mountain_list.count(mountain_list[0]):
        Mount_equal = True
    # если есть плоскогорье - одинаковые элемнты
    if len(set(list_up)) == len(list_down): Mount_flat = True

    if not (Mount_flat) and not (Mount_equal) and Mount_up and Mount_down:
        Mount_check = True


    # Обязательно печатаем результат, иначе Яндекс Контест не увидит решение!
    # print(Mount_check)
    return Mount_check



if __name__ == '__main__':
    # Решение оформлено в функцию, эту функцию надо обязательно вызвать:
    # Яндекс Контест не сможет вызвать её сам.
    main()



