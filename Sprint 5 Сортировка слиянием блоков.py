def input_data():
    '''input data from user'''
    sort_number : int = int(input())
    sort_list: list = [int(x) for x in input().split()]

    return sort_number, sort_list


def sort_by_bloks(sort_number:int, sort_list:list) -> int:
    '''sort by bloks'''
    bloks : int = 0

    idx = sort_list.index(0)

    for i in range(0, len(sort_list)):
        idx = sort_list.index(0)








if __name__ == '__main__':
    (sort_number, sort_list) = input_data(), # ввод данных
    result = sort_by_bloks(sort_number,sort_list) # создание массива
    #print (result)
    print(result)
