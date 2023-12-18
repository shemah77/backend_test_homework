class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


class FullTimeEmployee(Employee):
    vacation_days = 28
    def get_unpaid_vacation(self, unpaid_vacation: str, unpaid_days: int):
        return (f'Начало неоплачиваемого отпуска: {unpaid_vacation}, '
                f'продолжительность: {unpaid_days} дней.'
                )

    def __init__(self, first_name, second_name, gender):
        self.remaining_vacation_days = FullTimeEmployee.vacation_days
        super().__init__(first_name, second_name, gender)


class PartTimeEmployee(Employee):
    vacation_days = 14

    def __init__(self, first_name, second_name, gender):
        self.remaining_vacation_days = PartTimeEmployee.vacation_days
        super().__init__(first_name, second_name, gender)





# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee(gender='м', first_name='Rob', second_name='Cruso')
employee2 = Employee(gender='ж', first_name='Ira', second_name='Crusovkina')



# Допишите код для вывода информации о сотрудниках.
# print(f' Имя: {employee1.first_name},'
#       f' Фамилия: {employee1.second_name},'
#       f' Пол: {employee1.gender}, '
#       f'Отпускных дней в году: {employee1.vacation_days}.')
#
# print(f' Имя: {employee2.first_name},'
#       f' Фамилия: {employee2.second_name},'
#       f' Пол: {employee2.gender}, '
#       f'Отпускных дней в году: {employee2.vacation_days}.')
#
# employee1.consume_vacation(7)
# print (employee1.get_vacation_details())

# Пример использования:
full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')


# print(part_time_employee.vacation_days)

# print(full_time_employee.vacation_days)


print(part_time_employee.get_vacation_details())