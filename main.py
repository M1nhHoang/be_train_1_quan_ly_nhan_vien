from services.employees_service import Employees_service
from prettytable import PrettyTable


def count_employees_table(employees_manager):
    # Create header
    headers = ["Tổng số nhân viên"]

    # Init table
    table = PrettyTable(headers)

    # Create row
    table.add_row([employees_manager.count_employees()])

    print(table)


def count_by_gender_table(employees_manager):
    # Create header
    headers = ["Giới tính", "Tổng số nhân viên"]

    # Init table
    table = PrettyTable(headers)

    # Create row
    gender_count = employees_manager.count_by_gender()
    print
    table.add_row(["Nam", gender_count['male']])
    table.add_row(["Nữ", gender_count['female']])

    print(table)


def max_salary_table(employees_manager):
    # Create header
    headers = [
        "ID",
        "First Name",
        "Last Name",
        "Email",
        "Phone",
        "Gender",
        "Age",
        "Job Title",
        "Years Of Experience",
        "Salary",
        "Department"]

    # Init table
    table = PrettyTable(headers)
    table._title = "Nhân viên có lương cao nhất"

    # Create row
    salary_employee = employees_manager.max_salary()
    table.add_row([
        salary_employee._id,
        salary_employee._first_name,
        salary_employee._last_name,
        salary_employee._email,
        salary_employee._phone,
        salary_employee._gender,
        salary_employee._age,
        salary_employee._job_title,
        salary_employee._years_of_experience,
        salary_employee._salary,
        salary_employee._department
    ])

    print(table)


def min_salary_table(employees_manager):
    # Create header
    headers = [
        "ID",
        "First Name",
        "Last Name",
        "Email",
        "Phone",
        "Gender",
        "Age",
        "Job Title",
        "Years Of Experience",
        "Salary",
        "Department"]

    # Init table
    table = PrettyTable(headers)
    table._title = "Nhân viên có lương thấp"

    # Create row
    salary_employee = employees_manager.min_salary()
    table.add_row([
        salary_employee._id,
        salary_employee._first_name,
        salary_employee._last_name,
        salary_employee._email,
        salary_employee._phone,
        salary_employee._gender,
        salary_employee._age,
        salary_employee._job_title,
        salary_employee._years_of_experience,
        salary_employee._salary,
        salary_employee._department
    ])

    print(table)


def max_years_of_experience_table(employees_manager):
    # Create header
    headers = [
        "ID",
        "First Name",
        "Last Name",
        "Email",
        "Phone",
        "Gender",
        "Age",
        "Job Title",
        "Years Of Experience",
        "Salary",
        "Department"]

    # Init table
    table = PrettyTable(headers)
    table._title = "Nhân viên có kinh nghiệm nhiều nhất"

    # Create row
    salary_employee = employees_manager.min_salary()
    table.add_row([
        salary_employee._id,
        salary_employee._first_name,
        salary_employee._last_name,
        salary_employee._email,
        salary_employee._phone,
        salary_employee._gender,
        salary_employee._age,
        salary_employee._job_title,
        salary_employee._years_of_experience,
        salary_employee._salary,
        salary_employee._department
    ])

    print(table)


def youngest_oldest_table(employees_manager):
    # Create header
    headers = [
        "ID",
        "First Name",
        "Last Name",
        "Email",
        "Phone",
        "Gender",
        "Age",
        "Job Title",
        "Years Of Experience",
        "Salary",
        "Department"]

    youngest_oldest_employee = employees_manager.youngest_oldest()

    # Init table for youngest employee
    table_youngest = PrettyTable(headers)
    table_youngest._title = "Nhân viên trẻ nhất"

    # Create row
    youngest_employee = youngest_oldest_employee["youngest"]
    table_youngest.add_row([
        youngest_employee._id,
        youngest_employee._first_name,
        youngest_employee._last_name,
        youngest_employee._email,
        youngest_employee._phone,
        youngest_employee._gender,
        youngest_employee._age,
        youngest_employee._job_title,
        youngest_employee._years_of_experience,
        youngest_employee._salary,
        youngest_employee._department
    ])

    # Init table for oldest employee
    table_oldest = PrettyTable(headers)
    table_oldest._title = "Nhân viên lớn nhất"

    # Create row
    oldest_employee = youngest_oldest_employee["oldest"]
    table_oldest.add_row([
        oldest_employee._id,
        oldest_employee._first_name,
        oldest_employee._last_name,
        oldest_employee._email,
        oldest_employee._phone,
        oldest_employee._gender,
        oldest_employee._age,
        oldest_employee._job_title,
        oldest_employee._years_of_experience,
        oldest_employee._salary,
        oldest_employee._department
    ])

    print(table_youngest)
    print(table_oldest)


def sum_salary_table(employees_manager):
    # Create header
    headers = ["Tổng lương"]

    # Init table
    table = PrettyTable(headers)

    # Create row
    table.add_row([employees_manager.sum_salary()])

    print(table)


if __name__ == '__main__':
    try:
        employees_manager = Employees_service()
    # File not found exceptions
    except FileNotFoundError as fe:
        print(fe)
        exit(0)
    # Other exceptions
    except Exception as e:
        print(e)
        exit(0)

    while True:
        print('================ Menu ================')
        print('1. Tổng số nhân viên')
        print('2. Số nhân viên nữ/ số nhân viên nam')
        print('3. Nhân viên có lương cao nhất')
        print('4. Nhân viên có lương thấp nhất')
        print('5. Nhân viên có kinh nghiệm nhiều nhất')
        print('6. Nhân viên trẻ nhất và lớn nhất')
        print('7. Tổng số lương phải trả cho tất cả nhân viên')
        print('0. Thoát chương trình')
        print('======================================')

        option = input("\nNhập lựa chọn của bạn (0-7): ")
        match option:
            case '1':
                count_employees_table(employees_manager)
            case '2':
                count_by_gender_table(employees_manager)
            case '3':
                max_salary_table(employees_manager)
            case '4':
                min_salary_table(employees_manager)
            case '5':
                max_years_of_experience_table(employees_manager)
            case '6':
                youngest_oldest_table(employees_manager)
            case '7':
                sum_salary_table(employees_manager)
            case '0':
                break

        input()
