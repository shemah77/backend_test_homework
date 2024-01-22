

def main():
    # skobki_list = input().split()
    skobki_str = input() # Считали первую строку ввода.
    skobki_list = list(skobki_str)
    stek = []
    # print (skobki_str)
    # print (skobki_list)
    check_skobki = True
    for skobki in skobki_list:
        if skobki == '(' or skobki == '[' or skobki == '{':
            stek.append(skobki)
        elif skobki == ')' :
            if len(stek) > 0:
                last_item_stek = stek.pop(-1)
                # print (last_item_stek)
                if last_item_stek == '(':
                    check_skobki = True
                    continue
                else: check_skobki = False
            else: check_skobki = False
        elif skobki == ']':
            if len(stek) > 0:
                last_item_stek = stek.pop(-1)
                if last_item_stek == '[':
                    check_skobki = True
                    continue
                else: check_skobki = False
            else: check_skobki = False
        elif skobki =='}':
            if len(stek) > 0:
                last_item_stek =stek.pop(-1)
                if last_item_stek == '{':
                    check_skobki = True
                    continue
                else: check_skobki = False
            else:
                check_skobki = False

    if len (stek) >0 :
        # print(stek)
        check_skobki = False
    # Обязательно печатаем результат, иначе Яндекс Контест не увидит решение!
    # print(' '.join(result))
    print (check_skobki)



if __name__ == '__main__':
    # Решение оформлено в функцию, эту функцию надо обязательно вызвать:
    # Яндекс Контест не сможет вызвать её сам.
    main()
