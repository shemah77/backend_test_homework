# программа находит элементы массива которые дают заданную сумму
# и выводит их в виде списка - массива. Элементы могут быть не по порядку и не рядом
# и их может быть несколько как только программа находит одно решение она
# останавливается и решение может быть только одно
#
# Given a array of integers nums and an integer target,
# return indices of the two numbers such that the  add up to target.
#  You may assume that each input would have exactly one
# solution, and you may not use the same element twice.
#
# You
# can
# return the
# answer in any
# order.
#
# Example
# 1:
#
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because
# nums[0] + nums[1] == 9, we
# return [0, 1].
# Example
# 2:
#
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Example
# 3:
#
# Input: nums = [3, 3], target = 6
# Output: [0, 1]

def two_summ(array_inp: list, total: int):
    # -> list:
    sum_t = total
    new_list = sorted(array_inp, reverse=True)
    fin_list = []
    fin_list2 = []  # фин список элементов позиции в изначальном массиве

    list_position = {}

    for i in range(0, len(array_inp)):  # словарь где запоминаем позицию элемент
        list_position[i] = array_inp[i]

    for j in range(0, len(new_list)):
        if sum_t > 0:
            if new_list[j] > sum_t:
                pass
            elif new_list[j] <= sum_t:
                fin_list.append(new_list[j])
                sum_t = sum_t - new_list[j]

    for item in range(0, len(fin_list)):
        for key in list(list_position.keys()):
            if list_position[key] == fin_list[item]:
                fin_list2.append(key)
                del list_position[key]

        # for key, value in list_position.items():
        #    if fin_list[item] == value:
        #        if len (fin_list)  - len(fin_list2) > 0 :
        #            fin_list2.append(key)
        #            list_position[key] = None
        #            fin_list [item] = None

    return sum_t, fin_list, sorted(fin_list2)


list1 = [2, 7, 11, 15]
total1 = 9

list2 = [3, 2, 4]
total2 = 6

list3 = [3, 3]
total3 = 6

# list3 = [2, 0, 3, 10, 18, 48, 12, 0, 2, 2, 3,]
# total3 = 36


# print (two_summ(list1, total1))
print(f' total: {total1}')
print(two_summ(list1, total1))

print(f' total: {total2}')
print(two_summ(list2, total2))

print(f' total: {total3}')
print(two_summ(list3, total3))
