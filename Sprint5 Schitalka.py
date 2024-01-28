
def input_data():
    '''input data from user'''
    N_count: int = int(input()) # кол-во претендентов
    K_count: int = int(input()) # кол-во тактов в считалке

    # N_queue = LimitedQueue(N_count)
    N_list = [] # list of candidates

    for _ in range(1, N_count+1):
        N_list.append(f'{_}й astronaut')
        # N_queue.push(f'{_} astronaut')
    return N_list, K_count

def rec_count(N_list, Start_count, Max_count):
    '''Recursive'''
    N_list_len = len(N_list)
    # print (f'указываем на {N_list[Start_count]} это по считалочке {Start_count}й,из  {Max_count}, а всего их {N_list_len}')


    # base case
    if Start_count >= Max_count:
        # print(N_list[Max_count % N_list_len])
        # print('Stop at ' + str(Max_count) , str(Start_count), str((N_list[Max_count % len(N_list)])))
        # print(f'конец считалочки! выбран {N_list[(Start_count % len(N_list))-1]}') # выибрает элемент массива

        return Start_count % len(N_list)-1

    # recursive case
    else:
        if Start_count >= len(N_list):
            i = Start_count % len(N_list)
            # print (i)
        else:
            i = Start_count
            # print (i)

        # print(f'Эни бет счет до {Max_count} Считем и {N_list[i]} шаг {Start_count}')
        return rec_count(N_list, Start_count+1, Max_count)


# нерабочий алгоритм
def choose_austro(N_list, K_count): # выбирем астронавта
    '''sort N list by K elements using '''

    # print(N_list,K_count)
    Start_count = 0
    Max_count = K_count
    Choosed_austro = 0
    Pointer = None
    while len(N_list)>1:
        # base case
        if Start_count >= Max_count:
            # print(N_list[Max_count % N_list_len])
            # print('Stop at ' + str(Max_count) , str(Start_count), str((N_list[Max_count % len(N_list)])))
            # print(f'конец считалочки! выбран {N_list[(Start_count % len(N_list))-1]}') # выибрает элемент массива

            print(f'{N_list[Choosed_austro]} - point on  you! out of team ! {Start_count}')
            Choosed_austro = Start_count % len(N_list)

            Pointer  = Choosed_austro
            Start_count = 0



            N_list.pop(Choosed_austro)



        # recursive case
        else:
            if Pointer is not None:
                Start_count = 0
                print (f'{N_list[Pointer]} - продолжаем там где остановились Счетчик на {Start_count}')

                Pointer = None


            else:

                if Start_count >= len(N_list):
                    i = Start_count % len(N_list)
                    print (f'считаем по след кругу  {N_list[i]} счетчик на {Start_count}')
                else:
                    i = Start_count
                    print (f'считаем {N_list[i]} счетчик {Start_count}')
        Start_count +=1

    return N_list
# нерабочий алгоритм
def choose_astronauts(N_list, K_count): #  выбираем астронавта
    '''если K < N'''
    if K_count < len(N_list):
     while len(N_list) > 1:
        for i in range(1, K_count):
            print (N_list)
            if i == K_count:
                N_list.pop(i)
    return N_list

# рабочий алгоритм

def flavia(N_list, K_count):
    alive = [True] * len(N_list)
    n = len(N_list)
    k = K_count
    num_survivors, current_position, index = n, 0, 0
    while num_survivors:
        if alive[current_position]:
            index += 1
            if index == k:
                num_survivors = num_survivors - 1
                if not num_survivors:
                    return current_position+1
                else:
                    alive[current_position] = False
                    index = 0
        current_position = (current_position + 1) % n





if __name__ == '__main__':
    N_list,  K_count = input_data()
    # a = flavia(N_list, K_count)
    b = choose_austro(N_list, K_count)
    #b = choose_astronauts(N_list,K_count)
    # print (a)
    # print (b)

    # print (a)
    print (b)
    #print (int(x[0]))







