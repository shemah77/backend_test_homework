class Employee:
    # Вместо инструкции pass напишите свой код.
    vacation_days = 28

    def __init__(self, gender, first_name, second_name):
        self.gender = gender
        self.first_name = first_name
        self.second_name = second_name
        self.remaining_vacation_days = Employee.vacation_days


    def consume_vacation(self, consumed_days:int):
        self.remaining_vacation_days -= consumed_days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}'




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

employee1.consume_vacation(7)
print (employee1.get_vacation_details())


