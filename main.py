from statistics import mean #подключил встроенную функцию Mean из библиотеки statistics


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
                if course in lector.lgrades: #проверка есть ли курс в списке ключей словаря lgrades
                    lector.lgrades[course] += [grade] #если есть - то в список оценок добавляется новая оценка
                else:
                    lector.lgrades[course] = [grade] #если нет - то создается новая пара ключ/оценка
            else:
                print("Оценка должна быть в диапазоне от 0 до 10!")
        else:
            print('Error!')

    def __avg_stud(self): #Метод для вычисления средней оценки
        sum_d = []
        for values in self.grades.values():
            sum_d.extend(values)
        avg = mean(sum_d)
        return avg

    def __str__(self):

        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {Student.__avg_stud(self)} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
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

    def __avg_lec(self): #Метод для вычисления средней оценки
        sum_d = []
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

Moriarty = Lecturer('Moriarty', 'Professor') #добавил лектора
Moriarty.courses_attached += ['Python'] #добавил ему курс в список крусов
Moriarty.courses_attached += ['Git']

Luthor = Lecturer('Lex', 'Luthor') #добавил лектора №2
Luthor.courses_attached += ['Python']
Luthor.courses_attached += ['Git']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'your_gender') #new student object
best_student.courses_in_progress += ['Python'] #new course in coureses
best_student.Lecturer_grade(Moriarty, 'Python', 10)
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

print(Moriarty)
print()
print(cool_mentor)
print()
print(best_student)
print()
print(Luthor)
print()
print(Moriarty < Luthor)