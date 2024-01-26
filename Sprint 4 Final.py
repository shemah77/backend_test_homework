# id задачи в Яндекс Контест 105875402
def input_data():
    '''input data from user'''
    robot_weight_array: list = [int(x) for x in input().split()]
    platform_limit: int = int(input())
    return robot_weight_array, platform_limit


def platform(robot_weight_array: list, platform_limit:int):
    '''This function for robot weight calculation and platform'''

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

    return number_of_platform


def main ():
    '''главная функция '''
    robot_weight_array, platform_limit = input_data()
    print(platform(robot_weight_array, platform_limit))



if __name__ == '__main__':
    # Решение оформлено в функцию, эту функцию надо обязательно вызвать:
    # Яндекс Контест не сможет вызвать её сам.
    main()
