class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    """Задание № 2. Атрибуты и взаимодействие классов.
    В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания. 
    Теперь это могут делать только Reviewer (реализуйте такой метод)! А что могут делать лекторы? 
    Получать оценки за лекции от студентов :) 
    Реализуйте метод выставления оценок лекторам у класса Student (оценки по 10-балльной шкале, 
    хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов, а значения – списки оценок).
    Лектор при этом должен быть закреплен за тем курсом, на который записан студент."""

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


    def avr_grade(self, course = None):
        if course == None:
            avr_grades = []
            for course_ in self.grades:
                avr_grades.append(sum(self.grades[course_]) / len(self.grades[course_]))
            return sum(self.grades[course_]) / len(self.grades[course_])
        else:
            return sum(self.grades[course]) / len(self.grades[course])

    """  Задание № 3. Полиморфизм и магические методы
    Перегрузите магический метод __str__ у всех классов.
    У проверяющих он должен выводить информацию в следующем виде:
        print(some_student)
        Имя: Ruoy
        Фамилия: Eman
        Средняя оценка за домашние задания: 9.9
        Курсы в процессе изучения: Python, Git
        Завершенные курсы: Введение в программирование
    """
    
    def __str__(self):
        return str(f'Имя: {self.name}\n' \
                   f'Фамилия: {self.surname}\n' \
                   f'Средняя оценка за домашние задания:{round(self.avr_grade(), 1)}\n' \
                   f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                   f'Завершенные курсы: {", ".join(self.finished_courses)}')

    '''Задание № 3. Полиморфизм и магические методы
    Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.
    '''
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

    def avr_grade(self, course=None):
        if course == None:
            avr_grades = []
            for course_ in self.grades:
                avr_grades.append(sum(self.grades[course_]) / len(self.grades[course_]))
            return sum(avr_grades) / len(avr_grades)
        else:
            return sum(self.grades[course]) / len(self.grades[course])

    """  Задание № 3. Полиморфизм и магические методы
    Перегрузите магический метод __str__ у всех классов.
    У проверяющих он должен выводить информацию в следующем виде:

            print(some_lecturer)
            Имя: Some
            Фамилия: Buddy
            Средняя оценка за лекции: 9.9
    """
    def __str__(self):
        return str(
            f'Имя: {self.name}\n'\
            f'Фамилия: {self.surname}\n'\
            f'Средняя оценка за лекции: {round(self.avr_grade(), 1)}')

    '''Задание № 3. Полиморфизм и магические методы
    Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.
    '''
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

    """ Задание № 2. Атрибуты и взаимодействие классов.
    В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания. 
    Теперь это могут делать только Reviewer (реализуйте такой метод)! А что могут делать лекторы? 
    Получать оценки за лекции от студентов :) 
    Реализуйте метод выставления оценок лекторам у класса Student (оценки по 10-балльной шкале, 
    хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов, а значения – списки оценок).
    Лектор при этом должен быть закреплен за тем курсом, на который записан студент."""

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    """  Задание № 3. Полиморфизм и магические методы
    Перегрузите магический метод __str__ у всех классов.
    У проверяющих он должен выводить информацию в следующем виде:

        print(some_reviewer)
        Имя: Some
        Фамилия: Buddy
    """
    def __str__(self):
        return str(f'Имя: {self.name}\nФамилия: {self.surname}')

'''
Задание № 4. Полевые испытания
Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:

для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).
'''
def students_avr_grade_by_course(students:list,course_tittle):
    avr_grades=[]
    for student in students:
        if isinstance(student, Student):
            avr_grades.append(student.avr_grade(course=course_tittle))
    return sum(avr_grades)/len(avr_grades)


def lectures_avr_grade_by_course(lectures:list,course_tittle):
    avr_grades = []
    for lecture in lectures:
        if isinstance(lecture, Lecture):
            avr_grades.append(lecture.avr_grade(course=course_tittle))
    return sum(avr_grades) / len(avr_grades)

if __name__=="__main__":
    # Test case Student
    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python', 'Voodoo']
    best_student.finished_courses += ['SpaceP0ker']

    strong_reviewer = Reviewer('John', 'Smith')
    strong_reviewer.courses_attached += ['Python', 'Voodoo']
    print('Задание № 3. Полиморфизм и магические методы\n', "print(some_reviewer)")
    print(strong_reviewer)

    strong_reviewer.rate_hw(best_student, 'Python', 10)
    strong_reviewer.rate_hw(best_student, 'Python', 8)
    strong_reviewer.rate_hw(best_student, 'Python', 9)

    strong_reviewer.rate_hw(best_student, 'Voodoo', 3)
    strong_reviewer.rate_hw(best_student, 'Voodoo', 1)
    strong_reviewer.rate_hw(best_student, 'Voodoo', 4)

    print("Задание № 3. Полиморфизм и магические методы\n", 'print(some_student)')
    print(best_student)

    cool_lector = Lecture('Some', 'Buddy')
    cool_lector.courses_attached += ['Python','Кулинария']

    best_student.rate_lector(cool_lector, 'Python', 10)
    best_student.rate_lector(cool_lector, 'Python', 9)
    best_student.rate_lector(cool_lector, 'Python', 9)
    print("Задание № 3. Полиморфизм и магические методы\n", 'print(some_lecturer)')
    print(cool_lector)

    dumb_student = Student('Lloyd', 'Christmas', 'not_sure')
    dumb_student.courses_in_progress += ['Voodoo']

    strong_reviewer.rate_hw(dumb_student, 'Voodoo', 1)
    strong_reviewer.rate_hw(dumb_student, 'Voodoo', 1)
    strong_reviewer.rate_hw(dumb_student, 'Voodoo', 2)

    print("Задание № 3. Полиморфизм и магические методы\n",'part2')
    print(f'is best_Student eq dumb_student: {best_student != dumb_student}')

    worst_lector = Lecture('Hannibal', 'Lecter')
    worst_lector.courses_attached += ['Кулинария']
    dumb_student.rate_lector(worst_lector, 'Кулинария', 1)
    dumb_student.rate_lector(cool_lector, 'Кулинария', 3)
    best_student.rate_lector(worst_lector, 'Кулинария', 2)
    best_student.rate_lector(cool_lector, 'Кулинария', 5)
    print("Задание № 3. Полиморфизм и магические методы\n", 'part2')
    print(f'is cool_lector eq worst_lector: {cool_lector != worst_lector}')

    print('Задание № 4. Полевые испытания. Par#1')
    print(students_avr_grade_by_course([best_student,dumb_student],'Voodoo'))
    print('Задание № 4. Полевые испытания. Par#2')
    print(lectures_avr_grade_by_course([worst_lector, cool_lector], 'Кулинария'))

