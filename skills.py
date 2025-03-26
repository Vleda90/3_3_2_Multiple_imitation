class Student:
    @staticmethod
    def to_learn():
        print("I'm learning")


class Teacher:
    @staticmethod
    def to_teach():
        print("I'm teaching")


class StudentLead:
    @staticmethod
    def manage_group():
        print("I'm managing the group")


class Dean(Teacher):
    @staticmethod
    def manage_faculty():
        print("I'm managing the faculty")
