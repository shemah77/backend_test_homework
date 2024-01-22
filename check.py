def valid_mountain_array():
    mountain_list = [int(x) for x in input().split()]
    # Считали первую строку ввода.

    # target = int(input())
    # Считали вторую строку ввода.

    peak = max(mountain_list)
    peak_index = mountain_list.index(peak)
    list_up = mountain_list[:peak_index + 1]
    list_down = mountain_list[peak_index:]

    #print (list_up)
    #print (list_down)
    list_down_sorted  =  sorted(list_down, reverse = True)
    #print (list_down_sorted)


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
    if len(set(list_up)) != len(list_up): Mount_flat = True
    if len(set(list_down)) != len(list_down): Mount_flat = True

    if not (Mount_flat) and not (Mount_equal) and Mount_up and Mount_down:
        Mount_check = True

    if len(mountain_list) < 3:
        Mount_check = False
    if len(list_up) <= 1:
        Mount_check = False
    if len(list_down) <= 1:
        Mount_check = False


    # Обязательно печатаем результат, иначе Яндекс Контест не увидит решение!
    # print(Mount_check)
    return Mount_check

print (valid_mountain_array())



