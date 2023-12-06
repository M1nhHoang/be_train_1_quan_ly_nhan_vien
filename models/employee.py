class Employee:

    def __init__(self, **kwargs) -> None:
        self._id = kwargs.get('id')
        self._first_name = kwargs.get('first_name')
        self._last_name = kwargs.get('last_name')
        self._email = kwargs.get('email')
        self._phone = kwargs.get('phone')
        self._gender = kwargs.get('gender')
        self._age = kwargs.get('age')
        self._job_title = kwargs.get('job_title')
        self._years_of_experience = kwargs.get('years_of_experience')
        self._salary = kwargs.get('salary')
        self._department = kwargs.get('department')

    def __str__(self) -> str:
        return str({
            "id": self._id,
            "first_name": self._first_name,
            "last_name": self._last_name,
            "email": self._email,
            "phofne": self._phone,
            "gender": self._gender,
            "age": self._age,
            "job_title": self._job_title,
            "years_of_experience": self._years_of_experience,
            "salary": self._salary,
            "department": self._department
        })
