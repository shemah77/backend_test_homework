def length_of_longest_substring (string, substring):
    if len(string) == 0:
        return len(string)
    left, right = 0, len(string) - 1
    seen = {}
    pass
        

def main():
    # skobki_list = input().split()
    alien_str = input() # Считали первую строку ввода.
    alien_list  = list(alien_str)
    sub_alien = []
    alien_set = ()
    len_max = len(alien_str)
    max_len_sub = 0
    max_len_sub_ok = 0
    element_slice = 0
    window_sum = len(alien_list[0:element_slice])
    j = 0
    for index in range(element_slice, len(alien_list)):
        if alien_list[index] not in sub_alien:
            sub_alien.append(alien_list[index])






        # while element_slice <= len_max:
        #     window_sum = len(alien_list[element_slice]) - len(alien_list[element_slice-i])
        #
        #     alien_set = set(alien_list[i:i+element_slice])
        #     if len(alien_set) == window_sum:
        #         element_slice += 1
        #         max_len_sub_ok = len(alien_set)
        #     else:
        #         if len(alien_set) > max_len_sub:
        #             max_len_sub = len(alien_set)
        #         break




    # Обязательно печатаем результат, иначе Яндекс Контест не увидит решение!
    # print(' '.join(result))
    print (max(max_len_sub_ok, max_len_sub))



if __name__ == '__main__':
    # Решение оформлено в функцию, эту функцию надо обязательно вызвать:
    # Яндекс Контест не сможет вызвать её сам.
    main()
