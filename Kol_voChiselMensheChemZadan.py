def main():
    radioation_list = [int(x) for x in input().split()]  # Считали первую строку ввода.
    result = []
    # target = int(input()) # Считали вторую строку ввода.

    # если список одинаковый
    # if len (radioation_list) == radioation_list.count(radioation_list[0]):
    #     for i in range(len(radioation_list)):
    #         result[i] = 0
    for i in range(len(radioation_list)):
        count = 0 # считаем, сколько в массиве есть чисел,
                  # меньших, чем выбранное.
        for j in range(len(radioation_list)):
            if radioation_list[i] > radioation_list[j]:
                count = count + 1
        result.append(count)

    print(' '.join(map(str, result)))
    # Обязательно печатаем результат, иначе Яндекс Контест не увидит решение!
    # print(' '.join(result))

    # print(result)


if __name__ == '__main__':
    # Решение оформлено в функцию, эту функцию надо обязательно вызвать:
    # Яндекс Контест не сможет вызвать её сам.
    main()

