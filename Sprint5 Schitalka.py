
def input_data():
    '''input data from user'''
    N_count: int = int(input()) # кол-во претендентов
    K_count: int = int(input()) # кол-во тактов в считалке

    N_list = []

    for _ in range(1, N_count+1):
        N_list.append(f'{_} astronaut')
    return N_list, K_count

def rec_count(N_list, Start_count, Max_count):
    '''Recursive'''
    N_list_len = len(N_list)
    # print (f'указываем на {N_list[Start_count]} это по считалочке {Start_count}й,из  {Max_count}, а всего их {N_list_len}')


    # base case
    if Start_count >= Max_count:
        print(N_list[Max_count % N_list_len])
        print('Stop at ' + str(Max_count) , str(Start_count), str((N_list[Max_count % len(N_list)])))
        print(f'конец считалочки! выбран {N_list[(Start_count % len(N_list))]}') # выибрает элемент массива

        return (Start_count % len(N_list))

    # recursive case
    else:
        if Start_count >= len(N_list):
            i = Start_count % len(N_list)
            print (i)
        else:
            i = Start_count
            print (i)

        print(f'Эни бет счет до {Max_count} Считем и {N_list[i]} шаг {Start_count}')
        return rec_count(N_list, Start_count + 1, Max_count)







def choose_austro(N_list, K_count): # выбирем астронавта
    '''sort N list by K elements using '''
    N_final = 0 # финальный участник
    print(N_list,K_count)
    Start_count = 0
    while len (N_list) != 1:
        Choosed_austro = rec_count(N_list, Start_count , K_count)
        print (f'{Choosed_austro} - point on  you! out of team !')

        N_list.pop(Choosed_austro)
    return N_list












    return N_final
    pass




if __name__ == '__main__':
    N_list, K_count = input_data()
    a = choose_austro(N_list, K_count)
    print (a)


