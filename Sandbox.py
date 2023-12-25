
# Будет напечатано: 14

people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']


def say_to_all(func: object, sequence: object) -> object:
    for item in sequence:
        func(item)


# Этот вызов для каждого имени из списка должен напечатать
# строчку Привет, <имя>!
say_to_all(
            lambda people: print (f'Hi {people}')
            if people  == 'Соня' else print (f'Hello {people}'), people
           )


# print (f'Hi {people}') if people  == 'Соня' else print (f'Hello {people}')








# Этот вызов для каждого имени из списка должен напечатать
# строчку До завтра, <имя>!
# say_to_all(...)
