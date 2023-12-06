from models import Employee
from context import Context


class Employees_service:

    def __init__(self) -> None:
        # Create context
        try:
            self.__context = Context('./employees.json')
        # File not found exceptions
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{self._path}' does not exist.")
        # Other exceptions
        except Exception as e:
            raise Exception(e)

        # Read data
        self.__employees = [Employee(**data)
                            for data in self.__context.read_data()]

    def count_employees(self) -> int:
        return len(self.__employees)

    def count_by_gender(self) -> dict:
        gender_count = {
            'male': 0,
            'female': 0,
        }

        for employee in self.__employees:
            if employee._gender == 'male':
                gender_count['male'] += 1
            else:
                gender_count['female'] += 1

        return gender_count

    def max_salary(self) -> Employee:
        return max(self.__employees, key=lambda lamda: lamda._salary)

    def min_salary(self) -> Employee:
        return min(self.__employees, key=lambda lamda: lamda._salary)

    def max_years_of_experience(self) -> Employee:
        return max(
            self.__employees,
            key=lambda lamda: lamda._years_of_experience)

    def youngest_oldest(self) -> dict:
        return {
            "youngest": min(
                self.__employees,
                key=lambda lamda: lamda._age),
            "oldest": max(
                self.__employees,
                key=lambda lamda: lamda._age)}

    def sum_salary(self) -> float:
        return sum(employee._salary for employee in self.__employees)
