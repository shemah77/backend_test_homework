class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


class MobilePhone(Phone):
    # Переопределить значение атрибута line_type класса Phone.
    line_type = 'беспроводной'

    battery_type = 'Li-ion'

    # Конструктор класса MobilePhone с новым параметром — network_type.
    def __init__(self, dial_type_value, network_type):
        # Новый атрибут объекта.
        self.network_type = network_type
        # Вызов родительского конструктора.
        super().__init__(dial_type_value)

    def start_game(self):
        print('Игра запущена!')

    # Переопределить метод ring() класса Phone.
    def ring(self):
        print('Дзынь-дзынь!')


rotary_phone = Phone('дисковый')
mobile_phone = MobilePhone('сенсорный', 'LTE')

# Распечатать значение атрибута line_type для объекта класса Phone.
print(rotary_phone.line_type)
# Вызвать метод ring() для объекта класса Phone.
rotary_phone.ring()

# Распечатать значение атрибута line_type для объекта класса MobilePhone.
print(mobile_phone.line_type)
# Вызвать метод ring() для объекта класса MobilePhone.
mobile_phone.ring()
print(mobile_phone.network_type)
mobile_phone.start_game()

# Вывод:
# проводной
# Дзззззыыыыыыыынь!
# беспроводной
# Дзынь-дзынь!