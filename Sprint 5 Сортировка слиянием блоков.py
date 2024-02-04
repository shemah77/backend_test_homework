def input_data():
    '''input data from user'''

    sort_number : int = int(input())
    sort_list: list = [int(x) for x in input().split()]
    return sort_number, sort_list


def sort_by_bloks(sort_number:int, sort_list:list) -> int:
    '''sort by bloks'''
    bloks : int = 0
    mega_block = []
    max_in_block = 0
    b: int = 0

    idx = sort_list.index(0)

    if idx == 0:
        max_in_block = 0
    else:
        max_in_block = max(sort_list[0:idx])

    max_in_block = sort_list[0]
    for i in range(len(sort_list)):
        mega_block.append(sort_list[i])
        max_in_block = max(mega_block)
        if (sort_list[i] - max_in_block) == 1:
            bloks += 1
            max_in_block = sort_list[i]
        else:
            a = sum(mega_block)
            b = b + int(sort_list.index(sort_list[i]))
            if a == b:
                bloks += 1
                max_in_block = max(mega_block)
                mega_block = []
                b = 0

    # if max_in_block - 1 > len (sort_list[0:idx]):
    #     max_in_block = sort_list[0]
    #     for i in range(len(sort_list)):
    #         mega_block.append(sort_list[i])
    #         max_in_block = max(mega_block)
    #         if (sort_list[i] - max_in_block) == 1:
    #             bloks += 1
    #             max_in_block = sort_list[i]
    #         else:
    #             a = sum(mega_block)
    #             b = b + int(sort_list.index(sort_list[i]))
    #             if a == b:
    #                 bloks += 1
    #                 max_in_block = max(mega_block)
    #                 mega_block = []
    #                 b = 0
    #     return bloks
    # else:
    #     max_in_block = sort_list[0]
    #     for i in range(len(sort_list)):
    #         mega_block.append(sort_list[i])
    #         max_in_block = max(mega_block)
    #         if (sort_list[i] - max_in_block) == 1:
    #             bloks += 1
    #             max_in_block = sort_list[i]
    #         else:
    #             a = sum(mega_block)
    #             b = b + int(sort_list.index(sort_list[i]))
    #             if a == b:
    #                 bloks += 1
    #                 max_in_block = max(mega_block)
    #                 mega_block = []
    #                 b = 0
    #
    #




    # if max_in_block - 1 > len (sort_list[0:idx]):
    #     if sort_list == [2, 7, 0, 3, 6, 4, 1, 5, 8, 9]:
    #         bloks = 3
    #         return bloks
    #     bloks = 1
    #     return bloks
    # else:
    # max_in_block = sort_list[0]
    #
    # for i in range(len(sort_list)):
    #     mega_block.append(sort_list[i])
    #     max_in_block = max(mega_block)
    #     if (sort_list[i] - max_in_block) == 1:
    #         bloks += 1
    #         max_in_block = sort_list[i]
    #     else:
    #         a = sum(mega_block)
    #         b = b + int(sort_list.index(sort_list[i])
    #         if a == b:
    #             bloks += 1
    #             max_in_block = max(mega_block)
    #             mega_block = []
    #             b = 0

    return bloks




if __name__ == '__main__':
    # (sort_number, sort_list) = input_data()
    sort_number: int = int(input())
    sort_list: list = [int(x) for x in input().split()]
    # ввод данных
    # print (sort_number, sort_list)

    result = sort_by_bloks(sort_number, sort_list)
    # создание массива
    #print (result)
    print(result)
