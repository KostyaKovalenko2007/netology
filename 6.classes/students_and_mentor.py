class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecture) and course in lector.courses_attached and grade in range(1, 11, 1):
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [int(grade)]
        else:
            print(f'Some mistake while trying to rate lector: "{lector.name}, {lector.surname}"\n',
                  f'for course - "{course}" \n by grade = "{grade}"')
            return 'Ошибка'

    def avr_grade(self):
        avr_grades = []
        for course in self.grades:
            avr_grades.append(sum(self.grades[course]) / len(self.grades[course]))
        return sum(avr_grades) / len(avr_grades)

    def __str__(self):
        return str(f'Имя: {self.name}\n' \
                   f'Фамилия: {self.surname}\n' \
                   f'Средняя оценка за домашние задания:{round(self.avr_grade(), 1)}\n' \
                   f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                   f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __eq__(self, other):  # – для равенства ==
        if not isinstance(other, Student):
            raise TypeError("Операнд справа должен иметь тип Student")
        return self.avr_grade() == other.avr_grade()

    def __ne__(self, other):  # – для неравенства !=
        if not isinstance(other, Student):
            raise TypeError("Операнд справа должен иметь тип Student")
        return self.avr_grade() != other.avr_grade()

    def __lt__(self, other):  # – для оператора меньше <
        if not isinstance(other, Student):
            raise TypeError("Операнд справа должен иметь тип Student")
        return self.avr_grade() < other.avr_grade()

    def __le__(self, other):  # – для оператора меньше или равно <=
        if not isinstance(other, Student):
            raise TypeError("Операнд справа должен иметь тип Student")
        return self.avr_grade() <= other.avr_grade()

    def __gt__(self, other):  # – для оператора больше >
        if not isinstance(other, Student):
            raise TypeError("Операнд справа должен иметь тип Student")
        return self.avr_grade() > other.avr_grade()

    def __ge__(self, other):  # – для оператора больше или равно >=
        if not isinstance(other, Student):
            raise TypeError("Операнд справа должен иметь тип Student")
        return self.avr_grade() >= other.avr_grade()


class Mentor:
    name: str
    surname: str
    courses_attached = []

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecture(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}

    def avr_grade(self):
        avr_grades = []
        for course in self.grades:
            avr_grades.append(sum(self.grades[course]) / len(self.grades[course]))
        return sum(avr_grades) / len(avr_grades)

    def __str__(self):
        return str(
            f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.avr_grade(), 1)}')

    def __eq__(self, other):  # – для равенства ==
        if not isinstance(other, Lecture):
            raise TypeError("Операнд справа должен иметь тип Lecture")
        return self.avr_grade() == other.avr_grade()

    def __ne__(self, other):  # – для неравенства !=
        if not isinstance(other, Lecture):
            raise TypeError("Операнд справа должен иметь тип Lecture")
        return self.avr_grade() != other.avr_grade()

    def __lt__(self, other):  # – для оператора меньше <
        if not isinstance(other, Lecture):
            raise TypeError("Операнд справа должен иметь тип Lecture")
        return self.avr_grade() < other.avr_grade()

    def __le__(self, other):  # – для оператора меньше или равно <=
        if not isinstance(other, Lecture):
            raise TypeError("Операнд справа должен иметь тип Lecture")
        return self.avr_grade() <= other.avr_grade()

    def __gt__(self, other):  # – для оператора больше >
        if not isinstance(other, Lecture):
            raise TypeError("Операнд справа должен иметь тип Lecture")
        return self.avr_grade() > other.avr_grade()

    def __ge__(self, other):  # – для оператора больше или равно >=
        if not isinstance(other, Lecture):
            raise TypeError("Операнд справа должен иметь тип Lecture")
        return self.avr_grade() >= other.avr_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return str(f'Имя: {self.name}\nФамилия: {self.surname}')


# Test case Student
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Voodoo']
best_student.finished_courses += ['SpaceP0ker']

strong_reviewer = Reviewer('John', 'Smith')
strong_reviewer.courses_attached += ['Python', 'Voodoo']
# print(strong_reviewer)

strong_reviewer.rate_hw(best_student, 'Python', 10)
strong_reviewer.rate_hw(best_student, 'Python', 8)
strong_reviewer.rate_hw(best_student, 'Python', 9)

strong_reviewer.rate_hw(best_student, 'Voodoo', 3)
strong_reviewer.rate_hw(best_student, 'Voodoo', 1)
strong_reviewer.rate_hw(best_student, 'Voodoo', 4)
# print(best_student)

cool_lector = Lecture('Some', 'Buddy')
cool_lector.courses_attached += ['Python']

best_student.rate_lector(cool_lector, 'Python', 10)
best_student.rate_lector(cool_lector, 'Python', 9)
best_student.rate_lector(cool_lector, 'Python', 9)
# print(cool_lector)

dumb_student = Student('Lloyd', 'Christmas', 'not_sure')
dumb_student.courses_in_progress += ['Voodoo']

strong_reviewer.rate_hw(dumb_student, 'Voodoo', 1)
strong_reviewer.rate_hw(dumb_student, 'Voodoo', 1)
strong_reviewer.rate_hw(dumb_student, 'Voodoo', 2)
# print(dumb_student)
# print(f'is best_Student eq dumb_student: {best_student != dumb_student}')

worst_lector = Lecture('Hannibal', 'Lecter')
worst_lector.courses_attached += ['Кулинария']
dumb_student.rate_lector(worst_lector, 'Кулинария', 1)
best_student.rate_lector(worst_lector, 'Кулинария', 2)
print(f'is cool_lector eq worst_lector: {cool_lector != worst_lector}')
