import datetime
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'

goods = {}
goods = {
    'Яйца': [
        {'amount': Decimal(
            '4'), 'expiration_date': datetime.date(2023, 7, 15)},
        {'amount': Decimal('10'), 'expiration_date': datetime.date(2023, 8, 1)}
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ]
}


def add(items, title, good_amount, expiration_date=None):
    Batch = {}  # покупка словарь содержит кол-во amount  и срок годности expiration date
    list_of_prod = []  # лист покупок к одному title
    if '.' in str(good_amount):  # проверка точки в числе - дробное или целое ?
        amount2 = round(good_amount, 1)
    else:
        amount2 = good_amount
    if not type(expiration_date) == datetime.date and not expiration_date == None:
        expiration_date = datetime.datetime.strptime(
            expiration_date, DATE_FORMAT).date()

    Batch = {  # создаем  запись о покупке
        'amount': Decimal(amount2),
        'expiration_date': expiration_date
    }

    list_of_prod = [Batch]  # создаем запись о покупке в виде list
    # список всех ключей goods чтобы искать по неточному совпадению
    keys_list = list(items.keys())
    keys_list2 = []
    for key in keys_list:  # преобразование всех ключей в нижний регистр
        # keys_list[key] = str.lower(key)
        keys_list2.append(str.lower(key))
    # print (keys_list2)
    if str.lower(title) in keys_list2:  # если такой ключ уже есть
        for key in items:  # цикл перебирает  ключи в словаре
            if str.lower(title) == str.lower(
                    key):  # проверка соотвествия  в нижнем регистре записи и ключа (Яйца = яйца)
                # добавляет новую строку в существующий Title
                items[key].append(Batch)
    else:
        items[title] = list_of_prod


# =========================== конец функуции =============================
# ================== начало функции ==========
def add_by_note(items, note):
    note_list = note.split()  # сделали список из заметки
    # print (note)
    if '-' in note_list[-1]:
        # создает запись о покупке из списка с датой
        Batch = {'amount': Decimal(note_list[-2]),
                 'expiration_date': datetime.datetime.strptime(note_list[-1], DATE_FORMAT).date()}
        # создает запись о покупке из списка без даты
    else:
        Batch = {'amount': Decimal(note_list[-1]), 'expiration_date': None}
    title = ''
    if len(note_list) > 3:
        for i in range(0, len(note_list) - 2):
            title = title + note_list[i] + ' '
    else:
        title = note_list[0]
    title = title.rstrip()

    # print(note_list)

    list_of_prod = [Batch]  # создаем запись о покупке в виде list
    # список всех ключей goods чтобы искать по неточному совпадению
    keys_list = list(items.keys())
    keys_list2 = []
    for key in keys_list:  # преобразование всех ключей в нижний регистр
        # keys_list[key] = str.lower(key)
        keys_list2.append(str.lower(key))
    # print (keys_list2)
    if str.lower(title) in keys_list2:  # если такой ключ уже есть
        for key in items:  # цикл перебирает  ключи в словаре
            if str.lower(title) == str.lower(
                    key):  # проверка соотвествия  в нижнем регистре записи и ключа (Яйца = яйца)
                # добавляет новую строку в существующий Title
                items[key].append(Batch)
    else:
        items[title] = list_of_prod


# ================== конец функции


def find(items, needle):
    seach_list = []
    needle = str.lower(needle)

    for key in items.keys():

        if needle in str.lower(key):
            seach_list.append(key)
    return seach_list
    pass


# ================== конец find

# ============ начало amount
def amount(items, needle):
    needle = str.lower(needle)
    Sum = Decimal
    Sum = 0
    if needle == '':  # сумма всех продуктов - если имя продукта не задано
        for key in items.keys():  # перебор всех проуктов
            for i in items[key]:  # перебор всех словарей -покупок внутри одного продукта
                Sum = Sum + i['amount']

    for key in items.keys():
        if needle in str.lower(key):
            for i in items[key]:
                Sum = Sum + i['amount']

    return Decimal(Sum)


# =========== конец amount


def expire(items, in_advance_days=0):
    expiration_list = []
    Sum = Decimal
    Sum = 0
    DeadLine = datetime.date.today() + datetime.timedelta(days=in_advance_days)
    for title, parts in items.items():  # перебор всех проуктов
        Sum = 0
        for i in parts:  # перебор всех словарей -покупок внутри одного продукта
            # Sum = 0
            if i['expiration_date'] and i['expiration_date'] <= DeadLine:
                Sum = Sum + i['amount']
        if Sum > 0:
            # Expir_block = (title, Decimal(Sum))
            expiration_list += [(title, Decimal(Sum))]
    return expiration_list


# =============== окончание функции ============

# ========== тестирование ==========
add(goods, 'яйца', Decimal('10'), datetime.date(1999, 9, 30))
add(goods, 'яйца деревенские', Decimal('12'), datetime.date(2020, 8, 11))

# add(goods,'вода',Decimal(2.3))
# add(goods,'кофе',Decimal(0.25),'2124-1-30')
add_by_note(goods, 'яйца 2 2021-7-12')
print(goods)
print(find(goods, 'яйца'))
print(amount(goods, 'яйца'))
# Вывод: 1
print(amount(goods, 'морковь'))
# Вывод: 5
print(amount(goods, ''))
print(expire(goods, ))
print(print(expire(goods, 10)))
