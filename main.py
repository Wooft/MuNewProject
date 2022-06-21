from statistics import mean  # подключил встроенную функцию Mean из модуля statistics


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def Lecturer_grade(self, lector, course, grade):
        if course in lector.courses_attached:
            if 0 <= grade <= 10:
                if course in lector.lgrades:  # проверка есть ли курс в списке ключей словаря lgrades
                    lector.lgrades[course] += [grade]  # если есть - то в список оценок добавляется новая оценка
                else:
                    lector.lgrades[course] = [grade]  # если нет - то создается новая пара ключ/оценка
            else:
                print("Оценка должна быть в диапазоне от 0 до 10!")
        else:
            print('Error!')

    def __avg_stud(self):  # Метод для вычисления средней оценки
        sum_d = []
        if not self.grades:
            return ('Оценок нет')
        else:
            for values in self.grades.values():
                sum_d.extend(values)
            avg = mean(sum_d)
        return avg

    def __str__(self):

        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {Student.__avg_stud(self)} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Не студент!")
            return
        return Student.__avg_stud(self) < Student.__avg_stud(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lgrades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print(f"{other} не явялется лектором!")
            return
        return

    def __avg_lec(self):  # Метод для вычисления средней оценки
        sum_d = []
        if not self.lgrades:
            print('Оценок нет')
        else:
            for values in self.lgrades.values():
                sum_d.extend(values)
            avg = mean(sum_d)
        return avg

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {Lecturer.__avg_lec(self)}\n '
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не лектор!")
            return
        return Lecturer.__avg_lec(self) < Lecturer.__avg_lec(other)


class Reviewer(Mentor):
    def __rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


Moriarty = Lecturer('Moriarty', 'Professor')  # добавил лектора
Moriarty.courses_attached += ['Python']  # добавил ему курс в список крусов
Moriarty.courses_attached += ['Git']

Luthor = Lecturer('Hannibal', 'Lecter')  # добавил лектора №2
Luthor.courses_attached += ['Python']
Luthor.courses_attached += ['Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']

verycool_mentor = Reviewer('Doctor', 'Who')
verycool_mentor.courses_attached += ['Python']

notabest_student = Student('John', 'Shepard', 'YourChoise')
notabest_student.courses_in_progress += ['Python']
notabest_student.Lecturer_grade(Moriarty, 'Python', 6)
notabest_student.Lecturer_grade(Luthor, 'Python', 5)

best_student = Student('Ruoy', 'Eman', 'your_gender')  # new student object
best_student.courses_in_progress += ['Python']  # new course in coureses
best_student.courses_in_progress += ['Git']
best_student.Lecturer_grade(Moriarty, 'Python', 10)
best_student.Lecturer_grade(Moriarty, 'Python', 11)
best_student.Lecturer_grade(Moriarty, 'Python', 9)
best_student.Lecturer_grade(Moriarty, 'Python', 7)
best_student.Lecturer_grade(Moriarty, 'Git', 4)
best_student.Lecturer_grade(Luthor, 'Python', 5)
best_student.Lecturer_grade(Luthor, 'Python', 7)
best_student.Lecturer_grade(Luthor, 'Python', 6)
best_student.Lecturer_grade(Luthor, 'Git', 5)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Git', 8)
cool_mentor.rate_hw(best_student, 'Git', 7)
verycool_mentor.rate_hw(notabest_student, 'Python', 7)
verycool_mentor.rate_hw(notabest_student, 'Python', 4)

students = [best_student, notabest_student, cool_mentor]


def avg_hw(students, course_name):  # функция для вычисления средней оценки студентов по курсу
    avg_g = 0  # переменная для хранения среднего значения
    list_g = []  # пустой список для хранения оценок
    for stu in students:  # распаковка списка
        if isinstance(stu,
                      Student) and course_name in stu.courses_in_progress:  # если элемент списка принаджлежит классу Student, то выполняем код дальше
            for keys, values in stu.grades.items():  # распковка словаря с оценками
                if course_name == keys:  # если название курса в функции совпадает с ключом словаря
                    list_g.extend(values)  # добавляем значения элемента в список всех оценок
    if len(list_g) > 0:
        avg_g = mean(list_g)  # вычисление среднего значения оценок
        return f'Средняя оценка всех студентов по курсу {course_name} равна: {avg_g}'
    else:
        return f'По курсу {course_name} еще нет оценок либо указано неверное название курса!'


lectors = [Luthor, Moriarty]


def avg_lhw(lectors, course_name):
    avg_lg = 0
    list_lg = []
    for lec in lectors:
        if isinstance(lec, Lecturer) and course_name in lec.courses_attached:
            for keys, values in lec.lgrades.items():
                if course_name == keys:
                    list_lg.extend(values)
    if len(list_lg) > 0:
        avg_lg = mean(list_lg)
        return f'Средняя оценка всех лекторов по курсу {course_name} равна: {avg_lg}'
    else:
        return f'По курсу {course_name} еще нет оценок, либо указано неверное название курса!'


print(Moriarty)
print()
print(cool_mentor)
print()
print(best_student)
print()
print(notabest_student)
print()
print(Luthor)
print()
print(verycool_mentor)
print()

print(avg_hw(students, 'Python'))
print(avg_lhw(lectors, 'Python'))
print(avg_lhw(lectors, 'Marketing'))
print(Moriarty < Luthor)
print(best_student > notabest_student)