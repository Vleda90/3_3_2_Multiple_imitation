import position, cooperation, skills


class Student(
    position.Person,
    skills.Student,
    cooperation.AsStudent
):
    def __init__(self, name:str, surname:str, sex:str, birth_date:str, salary:float):
        super().__init__(name, surname, sex, birth_date, salary)


class Teacher(
    position.Person,
    skills.Teacher,
    cooperation.AsWorker
):
    def __init__(self, name:str, surname:str, sex:str, birth_date:str, salary:float):
        super().__init__(name, surname, sex, birth_date, salary)


class StudentLead(
    position.Person,
    skills.StudentLead,
    skills.Student,
    cooperation.AsStudent
):
    def __init__(self, name:str, surname:str, sex:str, birth_date:str, salary:float):
        super().__init__(name, surname, sex, birth_date, salary)





if __name__ == '__main__':
    st1 = Student('John', 'Smith', 'Male', '10-10-1999', 500)
    print(st1.get_salary_payment())
    te1 = Teacher('Amanda', 'Joins', 'Female', '10-10-1980', 10000)
    print(te1.birth_date)
    sl1 = StudentLead('Nick', 'McLovin', 'Male', '05-05-1998', 700)
    print(sl1.manage_group())
