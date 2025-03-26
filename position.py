from datetime import datetime
class Person:
    def __init__(self, name:str, surname:str, sex:str, birth_date_or_age:str, salary:float):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.salary = salary
        if isinstance(birth_date_or_age, int):
            today = datetime.today()
            birth_year = today.year - birth_date_or_age
            self._birth_date = datetime(birth_year, today.month, today.day)
        elif isinstance(birth_date_or_age, str):
            try:
                self._birth_date = datetime.strptime(birth_date_or_age, '%d-%m-%Y')
            except ValueError:
                raise ValueError('Birth date must be in "DD-MM-YYYY" format.')
        else:
            raise TypeError('birth_date_or_age must be an int or in "DD-MM-YYYY" format.')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('First name must be a string.')
        self._name = value.title()

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError('Last name must be a string.')
        self._surname = value.title()

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        if isinstance(value, str):
            try:
                self._birth_date = datetime.strptime(value, '%d-%m-%Y')
            except ValueError:
                raise ValueError('Birth date must be in "DD-MM-YYYY" format.')
        elif isinstance(value, datetime):
            self._birth_date = value
        else:
            raise TypeError('Birth date must be a string or in "DD-MM-YYYY" format.')

    @property
    def age(self):
        if self._birth_date is None:
            return None
        today = datetime.today()
        return today.year - self._birth_date.year - (
                (today.month, today.day) < (self._birth_date.month, self._birth_date.day)
        )

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")
        today = datetime.today()
        birth_year = today.year - value
        self._birth_date = datetime(birth_year, today.month, today.day)

    @age.deleter
    def age(self):
        print("Age deleted!")
        self._birth_date = None

    def __repr__(self):
        return f'{self.name} {self.surname} {self.age} {self.salary}'

    def __hash__(self):
        return hash((self.name, self.surname, self.age, self.salary))

    def __eq__(self, other):
        return (isinstance(other, Person)
                and self.name == other.name
                and self.surname == other.surname
                and self.salary == other.salary
                and self.age == other.age
        )


