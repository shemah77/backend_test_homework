import hashlib
example_array = [6, 5, 1, 3, 8, 7, 2, 4]

def bubble_sort(data):
    last_index = len(data) - 1
    while last_index >= 0:
        swapped = False
        for item_index in range(last_index):
            if data[item_index] > data[item_index+1]:
                data[item_index], data[item_index+1] = (
                    data[item_index +1], data[item_index]
                )
                swapped = True
        if swapped == True:
            last_index -= 1
        else: return data

    # Напишите здесь код сортировки.
    return data




# a ='https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'
# hash_md5 = hashlib.new('md5')
# a = a.encode('utf-8')
# print (a)
#
# hash_md5.update(a)
# # print (hash_md5)
# print(hash_md5.hexdigest())


# a = hashlib.sha256('https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html')
# print (a)


def find_two_indexes(data, expected_sum):
    # Ваше решение?
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if expected_sum == data[i] + data[j]:
                return (i,j)


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))


