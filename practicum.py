class Employee:
    # Вместо инструкции pass напишите свой код.
    vacation_days = 28

    def __init__(self, gender, first_name, second_name):
        self.gender = gender
        self.first_name = first_name
        self.second_name = second_name

    pass

# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee(gender='м', first_name='Rob', second_name='Cruso')
employee2 = Employee(gender='ж', first_name='Ira', second_name='Crusovkina')



# Допишите код для вывода информации о сотрудниках.
print(f' Имя: {employee1.first_name},'
      f' Фамилия: {employee1.second_name},'
      f' Пол: {employee1.gender}, '
      f'Отпускных дней в году: {employee1.vacation_days}.')

print(f' Имя: {employee2.first_name},'
      f' Фамилия: {employee2.second_name},'
      f' Пол: {employee2.gender}, '
      f'Отпускных дней в году: {employee2.vacation_days}.')




