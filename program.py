class Phone:
    # Атрибут класса.
    line_type = 'проводной'

    def __init__(self, dial_type_value):
        # Атрибут объекта.
        self.dial_type = dial_type_value


# Создать объект класса Phone.
rotary_phone = Phone(dial_type_value='дисковый')
keypad_phone = Phone(dial_type_value='кнопочный')

# Распечатать значение атрибута класса.
print(f'Тип линии: {rotary_phone.line_type}')
print(f'Тип линии: {keypad_phone.line_type}')

# Поменять значение атрибута line_type для объекта rotary_phone.
rotary_phone.line_type = 'радио'

# Снова распечатать значения.
print(f'Тип линии: {rotary_phone.line_type}')
print(f'Тип линии: {keypad_phone.line_type}')

# Поменять значение атрибута класса через класс.
Phone.line_type = 'спутниковый'

# Снова распечатать значения.
print(f'Тип линии: {rotary_phone.line_type}')
print(f'Тип линии: {keypad_phone.line_type}')

# Выведется:
# Тип линии: проводной
# Тип линии: проводной
# Тип линии: радио
# Тип линии: проводной
# Тип линии: радио
# Тип линии: спутниковый
print (dir(Phone))

