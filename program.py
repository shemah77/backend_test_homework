# Список для тестирования.

def MyRange (numbers):
    Sum = 0
    for i in range (0, len(numbers)):
        if numbers[i] % 3 == 0:
            yield numbers[i]**2


numbers = [1, 3, 4, 6, 9, 11]

# Здесь напишите ваше генераторное выражение.
simple_generator = (digit for digit in MyRange(numbers))

# Распечатайте сумму квадратов.
print (sum (simple_generator))





