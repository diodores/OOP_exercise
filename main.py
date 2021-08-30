class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        """Ставим оценку лектору"""
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [rate]
            else:
                lecturer.grades[course] = [rate]
        else:
            return 'Ошибка'

    def average_rating(self):
        """Возвращает средний балл"""
        mylist = []
        for grade in self.grades.values():
            for i in grade:
                mylist.append(i)
        average_rating = sum(mylist) / len(mylist)
        return average_rating


    def __lt__(self, other):
        """Сравниваем студентов по критерию - средний балл"""
        try:
            if not isinstance(other, Student):
                return 'Не корректные данные. Сравнить можно только оценки студентов.'
            elif other.average_rating() < self.average_rating():
                return f'Средний бал {self.name}, выше балла {other.name}'
            else:
                return f'Средний бал {other.name}, выше балла {self.name}'
        except IndentationError:
            print('Не корректные данные. Сравнить можно только оценки объектов однго класса.')
        except ZeroDivisionError:
            print('У одного из студентов отсутсвуют оценки.')


    def __str__(self):
        res = f'some_student\nИмя: {self.name}\nФамилия: {self.surname}\n \
        \rСредняя оценка за домашнее задание: {self.average_rating()}\n\
        \rКурсы в процессе изучения: {self.courses_in_progress}\n\
        \rЗавершенные курсы: {self.finished_courses}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        """Возвращает средний балл"""
        mylist = []
        for grade in self.grades.values():
            for i in grade:
                mylist.append(i)
        average_rating = sum(mylist) / len(mylist)
        return average_rating

    def __lt__(self, other):
        """Сравниваем лекторов по критерию - средний балл"""
        try:
            if not isinstance(other, Lecturer):
                return 'Не корректные данные. Сравнить можно только оценки лекторов.'
            elif other.average_rating() < self.average_rating():
                return f'Средний бал {self.name}, выше балла {other.name}'
            else:
                return f'Средний бал {other.name}, выше балла {self.name}'
        except IndentationError:
            print('Не корректные данные. Сравнить можно только оценки объектов однго класса.')
        except ZeroDivisionError:
            print('У одного из лекторов отсутсвуют оценки.')

    def __str__(self):
        res = f' some_lecturer\n Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {self.average_rating()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        """Ставим оценку студенту"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Определим вывод данных"""
        res = f' some_reviewer\n Имя: {self.name}\n Фамилия: {self.surname}'
        return res


student_1 = Student('Иван', 'Иванов', 'муж')
student_1.finished_courses += ['JS']
student_1.courses_in_progress += ['python', 'git']
student_2 = Student('Мария', 'Сидорова', 'жен')
student_2.finished_courses += ['js']
student_2.courses_in_progress += ['python', 'git']
lecturer_1 = Lecturer('Алексей', 'Федорович')
lecturer_1.courses_attached += ['python', 'git', 'js']
lecturer_2 = Lecturer('Андрей', 'Васильевич')
lecturer_2.courses_attached += ['python', 'git', 'js']
reviewer_1 = Reviewer('Дмитрий', 'Анатольевич')
reviewer_1.courses_attached += ['python', 'git', 'js']
reviewer_2 = Reviewer('Владимир' , 'Владимирович')
reviewer_2.courses_attached += ['python', 'git', 'js']
student_1.rate_lecturer(lecturer_1, 'python', 9)
student_1.rate_lecturer(lecturer_1, 'git', 10)
student_2.rate_lecturer(lecturer_1, 'python', 7)
student_2.rate_lecturer(lecturer_1, 'git', 9)
student_1.rate_lecturer(lecturer_2, 'python', 6)
student_1.rate_lecturer(lecturer_2, 'git', 8)
student_2.rate_lecturer(lecturer_2, 'python', 7)
student_2.rate_lecturer(lecturer_2, 'git', 9)
reviewer_1.rate_hw(student_1, 'python', 6)
reviewer_1.rate_hw(student_2, 'python', 4)
reviewer_1.rate_hw(student_1, 'git', 8)
reviewer_1.rate_hw(student_2, 'git', 7)
reviewer_2.rate_hw(student_2, 'python', 10)
reviewer_2.rate_hw(student_2, 'git', 7)
reviewer_2.rate_hw(student_1, 'python', 10)
reviewer_2.rate_hw(student_1, 'git', 7)
student_1.average_rating()
student_2.average_rating()
print(student_1 < student_2)
print('*********************')
print(f'{student_1}\n')
print(student_2)
print('*********************')
print(lecturer_1.average_rating())
print(lecturer_2.average_rating())
print('*********************')
print(lecturer_2 < lecturer_1)
print('*********************')
print(f'{lecturer_1}\n')
print(f'{lecturer_1}\n')
print(f'{reviewer_1}\n')
print(reviewer_2)
print('*********************')

students = [student_1, student_2]

def average_score_HW(students, course):
    """Возвращает общий средний балл за курс"""
    mylist = []
    for student in students:
        if student.grades.get(course) != None:
            for i in student.grades.get(course):
                mylist.append(i)
        else:
            pass
    average_score_HW = sum(mylist) / len(mylist)
    return average_score_HW

average_score_HW = average_score_HW(students, course='python')
print(f'Общий средний бал по курсу "python" составил: {average_score_HW}')
print('*******************')

lecturers = [lecturer_1, lecturer_2]

def average_score_L(lecturers, course):
    """Возвращает общий средний балл за курс лекторам"""
    mylist = []
    for lecturer in lecturers:
        if lecturer.grades.get(course) != None:
            for i in lecturer.grades.get(course):
                mylist.append(i)
        else:
            pass
    average_score_L = sum(mylist) / len(mylist)
    return average_score_L

average_score_L = average_score_L(lecturers, 'git')
print(f'Общий средний бал по курсу "git" поставленный лекторам составил: {average_score_HW}')




