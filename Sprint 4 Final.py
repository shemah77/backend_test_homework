def main():
    robot_weight_array: list = [int(x) for x in input().split()]  # массив роботов
    platform_limit: int = int(input())  # ограничение веса платформы
    number_of_platform: int = 0
    left: int = 0
    right: int = len(robot_weight_array)-1

    robot_weight_array.sort()

    while left <= right:
        if robot_weight_array[right] == platform_limit:
            number_of_platform += 1
            right -= 1
        elif (robot_weight_array[right] + robot_weight_array[left]) > platform_limit:
            number_of_platform += 1
            right -= 1
        elif (robot_weight_array[left] + robot_weight_array[right]) <= platform_limit:
            number_of_platform += 1
            left += 1
            right -= 1
        else:
            if left == right:
                number_of_platform += 1
            else:
                number_of_platform += 2
            left += 1
            right -= 1
    print(number_of_platform)


if __name__ == '__main__':
    # Решение оформлено в функцию, эту функцию надо обязательно вызвать:
    # Яндекс Контест не сможет вызвать её сам.
    main()
